# Usage Instructions for the `GoogleDriveManager` Class

The following instructions demonstrate how to use the [`GoogleDriveManager`](https://github.com/bot-wheels/bot-wheels-core/blob/main/src/utils/drive_manager.py) class to manage files on Google Drive. This class allows you to download, edit, and delete files in a selected Google Drive folder.

## 1. Initializing the Google Drive Manager

To use the class, you must first initialize it, which will authorize access to Google Drive:

```python
from DriveManager import GoogleDriveManager

drive_manager = GoogleDriveManager()
```

Access to the files is granted by [@Assassin-PL](https://github.com/Assassin-PL), who is the author of this code and the project administrator on Google Cloud. Users must be manually added as testers by [@Assassin-PL](https://github.com/Assassin-PL) and will receive the `credentials.json` file from them. The `token.pickle` file ensures that once the user has been added and the script has run successfully, there is no need to log in every time the script is used. After being added and running the script for the first time, users will be able to seamlessly download and interact with Google Drive within the entire project area by properly importing the [`GoogleDriveManager`](https://github.com/bot-wheels/bot-wheels-core/blob/main/src/utils/drive_manager.py) class.

## 2. Downloading a File from Google Drive

To download a file from Google Drive, you can use the [`open_file()`](https://github.com/bot-wheels/bot-wheels-core/blob/main/src/utils/drive_manager.py#120) method, which returns the content of the file with the given name:

```python
file_name = 'example.csv'
file_content = drive_manager.open_file(file_name)
if file_content:
    print(file_content.decode('utf-8'))
else:
    print(f"Plik '{file_name}' nie istnieje.")
```

This method verifies whether a file with the specified name exists within the folder and then retrieves its contents.

## 3. Uploading a File to Google Drive

To upload a file to Google Drive, you can use the [`upload_file()`](https://github.com/bot-wheels/bot-wheels-core/blob/main/src/utils/drive_manager.py#L92) method. If a file with the same name already exists, it will be updated. This method handles the necessary authorization and ensures that the file is correctly placed within the designated Google Drive folder.

```python
file_name = 'example.csv'
file_data = b"id,first_name,last_name\n1,John,Doe"
mime_type = 'text/csv'

drive_manager.upload_file(file_name, file_data, mime_type)
```

If the file already exists, its content will be updated; otherwise, a new file will be created.

## 4. Creating a New File

To create a new file in Google Drive, you can use the [`create_file()`](https://github.com/bot-wheels/bot-wheels-core/blob/main/src/utils/drive_manager.py#131) method, which works similarly to [`upload_file()`](https://github.com/bot-wheels/bot-wheels-core/blob/main/src/utils/drive_manager.py#L92):

```python
drive_manager.create_file(file_name, file_data, mime_type)
```

This method always creates a new file with the specified name. Ensure that the file name is unique within the target folder to avoid conflicts.

## 5. Listing Files

To display a list of files in a Google Drive folder, you can use the [`list_files()`](https://github.com/bot-wheels/bot-wheels-core/blob/main/src/utils/drive_manager.py#135) method:

```python
files = drive_manager.list_files()
for file in files:
    print(f"Nazwa: {file['name']}, ID: {file['id']}")
```

This method retrieves a list of files along with their names and identifiers. It provides an organized overview of all files within the specified folder, enabling easy access and management of your Google Drive contents.

## 6. Deleting a File

To delete a file from Google Drive, you must first obtain its identifier using the [`get_file_id()`](https://github.com/bot-wheels/bot-wheels-core/blob/main/src/utils/drive_manager.py#135) method, and then utilize the [`delete_file()`](https://github.com/bot-wheels/bot-wheels-core/blob/main/src/utils/drive_manager.py#148) method:

```python
file_id = drive_manager.get_file_id(file_name)
if file_id:
    drive_manager.delete_file(file_id)
    print(f"Plik '{file_name}' został usunięty.")
else:
    print(f"Plik '{file_name}' nie został znaleziony.")
```

This process involves retrieving the unique identifier of the desired file, which ensures that the correct file is targeted for deletion. Once the file ID is obtained, the [`delete_file()`](https://github.com/bot-wheels/bot-wheels-core/blob/main/src/utils/drive_manager.py#148) method removes the file from the specified Google Drive folder. This functionality allows for precise management of your Google Drive contents, enabling you to maintain an organized and up-to-date file structure by removing unnecessary or outdated files.

**Note:** Ensure that you have the necessary permissions to delete files and that you have correctly obtained the file ID to prevent accidental removal of important files.

## 7. Example Usage

To demonstrate the capabilities of the [`GoogleDriveManager`](https://github.com/bot-wheels/bot-wheels-core/blob/main/src/utils/drive_manager.py) class, the following example showcases how to check for the existence of a file, download it, edit its contents, and then upload it back to Google Drive:

```python
from utils.drive_manager import GoogleDriveManager
from data_generator import DataGen  # Assuming DataGen is the correct class for data generation

# Initialize the Google Drive Manager
drive_manager = GoogleDriveManager()
file_name = 'dane.csv'

# Check if the file exists in Google Drive
file_id = drive_manager.get_file_id(file_name)

if file_id:
    # File exists, download and edit its content
    file_content = drive_manager.open_file(file_name)
    csv_content = file_content.decode('utf-8')  # Decode the file content from bytes to string

    # Initialize the data generator and load existing data from CSV
    data = DataGen()
    data.from_csv_string(csv_content)  # Load data from the CSV string
    data.edit_data()  # Perform desired edits to the data
    updated_csv_content = data.to_csv_string().encode('utf-8')  # Convert the updated data back to CSV string and encode to bytes

    # Upload the updated file back to Google Drive, replacing the existing file
    drive_manager.upload_file(file_name, updated_csv_content, 'text/csv')
else:
    # File does not exist, create a new one
    data = DataGen()
    data.generate_data(num_records=20)  # Generate new data with 20 records
    csv_content = data.to_csv_string().encode('utf-8')  # Convert the generated data to CSV string and encode to bytes

    # Create a new file in Google Drive with the generated CSV content
    drive_manager.create_file(file_name, csv_content, 'text/csv')
```
