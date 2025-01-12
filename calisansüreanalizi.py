import numpy as np
import cv2

def analyze_employee_times(times):
    """
    Çalışan sürelerini analiz eden fonksiyon.
    
    Args:
        times (list of float): Çalışan süreleri (saniye veya dakika cinsinden).
        
    Returns:
        dict: Ortalama süre, standart sapma ve %10 değer kaybıyla düzenlenmiş süreler.
    """
    if not times:
        return "Zaman verileri boş."

    # Ortalama ve standart sapma hesaplama
    mean_time = np.mean(times)
    std_dev = np.std(times)

    # %10 değer kaybını ekleyerek güncellenmiş süreleri hesapla
    adjusted_times = [time * 0.9 for time in times]

    return {
        "Ortalama Süre": mean_time,
        "Standart Sapma": std_dev,
        "Düzenlenmiş Süreler (%10 kayıp)": adjusted_times
    }

def extract_times_from_video(video_path):
    """
    Videodan çalışanların başlangıç ve bitiş zamanlarını alır.
    
    Args:
        video_path (str): Video dosyasının yolu.
        
    Returns:
        list of float: Çalışan süreleri (saniye cinsinden).
    """
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Video açılamadı!")
        return []

    times = []

    print("Başlangıç ve bitiş zamanlarını girin (saniye cinsinden):")
    while True:
        start = input("Başlangıç zamanı (veya 'q' ile çıkış): ")
        if start.lower() == 'q':
            break
        end = input("Bitiş zamanı: ")
        
        try:
            start = float(start)
            end = float(end)
            times.append(end - start)
        except ValueError:
            print("Lütfen geçerli bir sayı girin!")

    cap.release()
    return times

# Örnek kullanım
if __name__ == "__main__":
    video_path = input("Video dosyasının yolunu girin: ")
    employee_times = extract_times_from_video(video_path)
    
    if employee_times:
        results = analyze_employee_times(employee_times)

        print("Ortalama Süre: {:.2f}".format(results["Ortalama Süre"]))
        print("Standart Sapma: {:.2f}".format(results["Standart Sapma"]))
        print("Düzenlenmiş Süreler (%10 kayıp):", results["Düzenlenmiş Süreler (%10 kayıp)"])
    else:
        print("Hiçbir süre bilgisi alınamadı.")
