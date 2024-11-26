import pyaudio
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
import librosa
import queue
import threading



# 'https://tfhub.dev/google/yamnet/1'
# YAMNet 모델 로드
def load_yamnet_model():
    model_url = "yamnet-tensorflow2-yamnet-v1"
    model = hub.load(model_url)
    return model



# 오디오 데이터 처리 함수
def preprocess_audio(audio_data, sample_rate=16000):
    # librosa로 멜 스펙트로그램 계산
    audio_data = librosa.util.normalize(audio_data)  # 정규화
    mel_spectrogram = librosa.feature.melspectrogram(y=audio_data, sr=sample_rate, n_mels=64)
    mel_spectrogram_db = librosa.power_to_db(mel_spectrogram, ref=np.max)  # 데시벨로 변환
    mel_spectrogram_expanded = np.expand_dims(mel_spectrogram_db, axis=0)
    return mel_spectrogram_expanded



# 예측된 클래스 이름을 텍스트로 변환하는 함수
def get_class_names(predictions, top_n=3):
    # 클래스 파일 경로 점검
    class_map_path = hub.load("yamnet-tensorflow2-yamnet-v1").class_map_path
    print("Class map path:", class_map_path.numpy())  # 경로 출력하여 확인
    
    with open(class_map_path.numpy(), "r") as f:
        class_labels = [line.strip() for line in f.readlines()]
    
    top_indices = predictions.argsort()[-top_n:][::-1]
    return [(class_labels[idx], predictions[idx]) for idx in top_indices]




# 실시간 오디오 스트림을 받아 YAMNet 예측 수행
def process_audio_stream(model, audio_queue, sample_rate=16000):
    while True:
        audio_data = audio_queue.get()  # 오디오 데이터를 큐에서 가져옴
        print("Audio data received:", audio_data[:10])  # 첫 10개 샘플만 출력하여 데이터 확인
        mel_spectrogram = preprocess_audio(audio_data, sample_rate)
        
        # 예측 수행
        predictions = model(mel_spectrogram)  # 모델 예측
        print("Predictions:", predictions)  # 예측 결과 출력
        
        # 예측 결과 처리
        class_scores = predictions['scores'].numpy()[0]  # 클래스 점수
        print("Class scores:", class_scores)  # 클래스 점수 출력
        
        # 상위 예측 결과 가져오기
        top_predictions = get_class_names(class_scores)
        
        # 예측 결과를 텍스트로 정리
        result_text = "Predicted sounds:\n"
        for label, score in top_predictions:
            result_text += f"{label}: {score:.3f}\n"
        
        # 예측 결과 출력
        print(result_text)  # 예측 결과를 출력



# 실시간 오디오 캡처 및 처리 함수
def audio_callback(in_data, frame_count, time_info, status, audio_queue):
    audio_data = np.frombuffer(in_data, dtype=np.float32)
    audio_queue.put(audio_data)  # 큐에 오디오 데이터 추가
    return (None, pyaudio.paContinue)



# 메인 함수
def start_streaming(model):
    # 오디오 큐 생성
    audio_queue = queue.Queue()

    # PyAudio 객체 생성
    p = pyaudio.PyAudio()

    # 오디오 스트림 설정
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=16000,
                    input=True,
                    frames_per_buffer=1024,
                    stream_callback=lambda in_data, frame_count, time_info, status: 
                                     audio_callback(in_data, frame_count, time_info, status, audio_queue))

    # 별도 쓰레드를 만들어 실시간으로 오디오를 처리
    processing_thread = threading.Thread(target=process_audio_stream, args=(model, audio_queue))
    processing_thread.daemon = True
    processing_thread.start()

    # 스트리밍 시작
    # 스트리밍 상태 확인
    if stream.is_active():
        print("Streaming is active")
        stream.start_stream()
    else:
        print("Streaming is not active")

    # print("Streaming started...")
    # stream.start_stream()

    # 스트리밍 유지
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("Streaming stopped.")
        stream.stop_stream()
        stream.close()
        p.terminate()


if __name__ == "__main__":
    # YAMNet 모델 로드
    model = load_yamnet_model()

    # 실시간 오디오 스트리밍 시작
    start_streaming(model)
