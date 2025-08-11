import os

# KAYNAK klasör yolu (proje klasörünü buraya yaz)
SOURCE_FOLDER = "/Users/selimaksoy/Documents/ollama_langchain_case1"

# ÇIKTI dosyası
OUTPUT_FILE = "project.txt"

# Hangi dosya uzantılarını ekleyeceğiz
INCLUDE_EXTENSIONS = {".py", ".js", ".ts", ".html", ".css", ".json", ".txt", ".md", ".java", ".c", ".cpp", ".cs"}

# Dahil edilmeyecek klasörler
EXCLUDE_FOLDERS = {"venv", ".venv", "__pycache__", "node_modules"}

def project_to_text(source_folder, output_file):
    with open(output_file, "w", encoding="utf-8") as outfile:
        for root, dirs, files in os.walk(source_folder):
            # Gereksiz klasörleri çıkart
            dirs[:] = [d for d in dirs if d not in EXCLUDE_FOLDERS]

            for file in files:
                ext = os.path.splitext(file)[1].lower()
                if ext in INCLUDE_EXTENSIONS:
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, "r", encoding="utf-8", errors="ignore") as infile:
                            outfile.write(f"\n\n===== {file_path} =====\n\n")
                            outfile.write(infile.read())
                    except Exception as e:
                        print(f"Hata: {file_path} okunamadı. ({e})")

    print(f"Tüm kodlar '{output_file}' dosyasına aktarıldı.")

# Çalıştır
project_to_text(SOURCE_FOLDER, OUTPUT_FILE)
