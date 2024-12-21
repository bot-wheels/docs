# Instrukcja korzystania z klasy `GoogleDriveManager`

Poniższa instrukcja pokazuje, jak korzystać z klasy `GoogleDriveManager` do zarządzania plikami na Google Drive. Klasa ta umożliwia pobieranie, edytowanie oraz usuwanie plików w wybranym folderze Google Drive.

## 1. Inicjalizacja menedżera Google Drive

Aby skorzystać z klasy, należy ją najpierw zainicjalizować, co spowoduje autoryzację dostępu do Google Drive:

```python
from DriveManager import GoogleDriveManager

drive_manager = GoogleDriveManager()
```

Podczas inicjalizacji klasa korzysta z plików `token.pickle` i `credentials.json`, aby uzyskać poświadczenia dostępu.

## 2. Pobieranie pliku z Google Drive

Aby pobrać plik z Google Drive, można użyć metody `open_file()`, która zwraca zawartość pliku o podanej nazwie:

```python
file_name = 'example.csv'
file_content = drive_manager.open_file(file_name)
if file_content:
    print(file_content.decode('utf-8'))
else:
    print(f"Plik '{file_name}' nie istnieje.")
```

Metoda ta sprawdza, czy plik o danej nazwie istnieje w folderze, a następnie pobiera jego zawartość.

## 3. Przesyłanie pliku do Google Drive

Aby przesłać plik do Google Drive, możemy użyć metody `upload_file()`. Jeśli plik o tej samej nazwie już istnieje, zostanie zaktualizowany:

```python
file_name = 'example.csv'
file_data = b"id,first_name,last_name\n1,John,Doe"
mime_type = 'text/csv'

drive_manager.upload_file(file_name, file_data, mime_type)
```

Jeśli plik już istnieje, jego zawartość zostanie zaktualizowana; w przeciwnym wypadku zostanie utworzony nowy plik.

## 4. Tworzenie nowego pliku

Aby utworzyć nowy plik w Google Drive, możemy użyć metody `create_file()`, która działa podobnie do `upload_file()`:

```python
drive_manager.create_file(file_name, file_data, mime_type)
```

Ta metoda zawsze tworzy nowy plik o podanej nazwie.

## 5. Wyświetlanie listy plików

Aby wyświetlić listę plików w folderze Google Drive, możemy użyć metody `list_files()`:

```python
files = drive_manager.list_files()
for file in files:
    print(f"Nazwa: {file['name']}, ID: {file['id']}")
```

Metoda ta zwraca listę plików wraz z ich nazwami i identyfikatorami.

## 6. Usuwanie pliku

Aby usunąć plik z Google Drive, należy najpierw uzyskać jego identyfikator za pomocą metody `get_file_id()`, a następnie skorzystać z metody `delete_file()`:

```python
file_id = drive_manager.get_file_id(file_name)
if file_id:
    drive_manager.delete_file(file_id)
    print(f"Plik '{file_name}' został usunięty.")
else:
    print(f"Plik '{file_name}' nie został znaleziony.")
```

## 7. Przykładowe użycie

W celu zobrazowania możliwości klasy `GoogleDriveManager`, poniżej znajduje się przykładowy kod, który sprawdza istnienie pliku, pobiera go, edytuje, a następnie przesyła z powrotem na Google Drive:

```python
drive_manager = GoogleDriveManager()
file_name = 'dane.csv'

# Sprawdzenie, czy plik istnieje
file_id = drive_manager.get_file_id(file_name)

if file_id:
    # Plik istnieje, pobierz i edytuj zawartość
    file_content = drive_manager.open_file(file_name)
    csv_content = file_content.decode('utf-8')

    # Odczytaj dane z CSV, edytuj i zapisz ponownie
    dane = dane_gen()
    dane.from_csv_string(csv_content)
    dane.edit_data()
    updated_csv_content = dane.to_csv_string().encode('utf-8')
    drive_manager.upload_file(file_name, updated_csv_content, 'text/csv')
else:
    # Plik nie istnieje, utwórz nowy
    dane = dane_gen()
    dane.generate_data(num_records=20)
    csv_content = dane.to_csv_string().encode('utf-8')
    drive_manager.create_file(file_name, csv_content, 'text/csv')
```
