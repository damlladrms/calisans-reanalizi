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

def main_menu():
    while True:
        print("\n*** Çalışan Süre Analizi ***")
        print("1. Video Süresi Analizi Yap")
        print("2. Manuel Süre Girişi Yap")
        print("3. Çıkış")

        choice = input("Seçiminizi yapın: ")

        if choice == '1':
            video_path = input("Video dosyasının yolunu girin: ")
            employee_times = extract_times_from_video(video_path)
            if employee_times:
                results = analyze_employee_times(employee_times)
                print("Ortalama Süre: {:.2f}".format(results["Ortalama Süre"]))
                print("Standart Sapma: {:.2f}".format(results["Standart Sapma"]))
                print("Düzenlenmiş Süreler (%10 kayıp):", results["Düzenlenmiş Süreler (%10 kayıp)"])
            else:
                print("Hiçbir süre bilgisi alınamadı.")

        elif choice == '2':
            try:
                manual_times = input("Süreleri virgülle ayırarak girin (ör. 120, 130, 140): ")
                times = list(map(float, manual_times.split(',')))
                results = analyze_employee_times(times)
                print("Ortalama Süre: {:.2f}".format(results["Ortalama Süre"]))
                print("Standart Sapma: {:.2f}".format(results["Standart Sapma"]))
                print("Düzenlenmiş Süreler (%10 kayıp):", results["Düzenlenmiş Süreler (%10 kayıp)"])
            except ValueError:
                print("Lütfen geçerli bir giriş yapın!")

        elif choice == '3':
            print("Çıkış yapılıyor...")
            break

        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")

# Örnek kullanım
if __name__ == "__main__":
    main_menu()
