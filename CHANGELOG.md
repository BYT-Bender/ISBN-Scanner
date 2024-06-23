# Change Log

## [1.0.0] - YYYY-MM-DD
### Added
- Initial release of the ISBN Scanner app.
- Implemented barcode decoding using OpenCV and pyzbar.
- Displays live webcam feed with overlaid barcode detection.
- Extracts barcode data and type, displaying them on the screen and printing to console.
- Supports quitting the application by pressing 'q'.

## [2.0.0] - YYYY-MM-DD
### Added
- Enhanced functionality to retrieve detailed book information from ISBN using `requests` and `BeautifulSoup`.
- Integrated web scraping to fetch book details from ISBNsearch.org.
- Improved user interface to show book title and author when scanning valid ISBN-13 or ISBN-10 barcodes.

### Changed
- Refactored barcode scanning logic to differentiate between ISBN barcodes and other types.
- Improved error handling for web requests and parsing of book information.

### Fixed
- Resolved issues related to capturing and processing frames from the webcam.
- Fixed bugs associated with displaying and decoding certain barcode types.

## [3.0.0] - YYYY-MM-DD
### Added
- Introduced GUI using tkinter for a more user-friendly interface.
- Utilized Google Books API to fetch book details based on ISBN.
- Displays book title, author, publisher, and publish date dynamically in the GUI.
- Integrated image processing using PIL to display webcam feed in the GUI.
- Added functionality to show a warning message if book details are not found for a scanned ISBN.

### Changed
- Refactored the application structure to implement object-oriented programming (OOP) principles.
- Updated barcode processing to handle EAN-13 barcodes specifically for fetching book details.

### Fixed
- Improved overall GUI responsiveness and layout management.
- Fixed minor bugs related to text display and barcode decoding.

## [3.1.0] - YYYY-MM-DD
### Added
- Implemented saving scanned book details including timestamp to a CSV file (`scanned_books.csv`).
- Added a process box in the GUI to display real-time updates of scanned book entries.
- Introduced a listbox in the GUI to display scanned ISBNs along with their corresponding titles.

### Changed
- Adjusted GUI layout to include a listbox for displaying scanned ISBNs and titles alongside book details.
- Enhanced user interaction by providing a visual list of scanned books and their titles.

### Fixed
- Improved overall stability and performance of the application.
- Fixed minor bugs related to text display and CSV file handling.

## [3.2.0] - YYYY-MM-DD
### Added
- Implemented loading previously scanned books from the CSV file on application startup.

### Changed
- Enhanced user feedback with updated status messages displayed in the GUI.
- Optimized handling of duplicate barcode entries.

### Fixed
- Improved overall application stability and performance.
- Addressed issues related to file handling for saving and loading scanned books data.

## [3.3.0] - YYYY-MM-DD
### Added
- Implemented a PyQt5 GUI for the ISBN Scanner application.
- Added real-time video feed from the webcam using OpenCV.
- Added a process list to display real-time updates of scanned book entries.

### Changed
- Updated status messages displayed in the GUI for better user feedback during scanning and book details retrieval.
- Optimized layout and organization of PyQt5 widgets for improved usability.

### Fixed
- Improved barcode decoding handling to catch and log errors more effectively.
- Enhanced overall application stability and performance.

## [3.4.0] - YYYY-MM-DD
### Added
- Implemented barcode decoding using `pyzbar` library with specific symbol set to `ZBarSymbol.EAN13`.
- Introduced error handling for barcode decoding errors to improve application stability.
- Enhanced user feedback with QMessageBox for displaying warnings when book details are not found or when an entry already exists.
- Expanded details shown in QTextEdit for scanned books to include description, page count, genre, and language.
- Implemented data persistence using CSV file (`scanned_books.csv`) for storing scanned book data including timestamp.

### Changed
- Updated barcode decoding to focus only on EAN-13 symbols using `pyzbar` library.
- Optimized the layout of PyQt5 widgets for a more organized and user-friendly interface.
- Refactored barcode decoding function (`decode_barcodes`) to encapsulate barcode decoding logic and error handling.

### Fixed
- Addressed potential issues related to file handling and data serialization when saving and loading scanned books.
- Improved overall application stability and performance with PyQt5-based GUI improvements and error handling.

## [3.5.0] - YYYY-MM-DD
### Added
- Enhanced book details retrieval by fetching additional information such as description, page count, categories, and language from Google Books API.
- Implemented PyQt5 GUI components including QLabel, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout, QFrame, QListWidget, and QMessageBox for a user-friendly interface.
- Incorporated error handling for network requests and barcode decoding to improve application stability.
- Added real-time feedback using QMessageBox for notifying users about invalid barcodes or duplicate entries.

### Changed
- Updated barcode decoding to focus only on EAN-13 symbols using `pyzbar` library.
- Optimized layout and organization of PyQt5 widgets to improve usability and visual appeal.

### Fixed
- Addressed potential issues related to file handling and data serialization in `save_scanned_books` and `load_scanned_books` methods.
- Improved overall application performance and reliability through code refactoring and error handling enhancements.

## [3.6.0] - YYYY-MM-DD
### Added
- Implemented sound notifications using `winsound` module for different events: scan success, scan error, and status change.
- Added functionality to play beeping sounds on successful scan, scan error, and status change.
- Introduced a wrapper method `play_sound` to handle different sound types based on specific events in the application.
- Implemented functionality to display details of a selected book from the list by clicking on its entry in `book_list`.
- Updated PyQt5 signal connection (`itemClicked`) to trigger the display of book details on list item click.

### Changed
- Refactored `show_book_details` method to append book details to `details_text` and also add the scanned book to `process_list` for tracking scanned items.
- Refactored `update_frame` method to include sound notifications on successful scan, duplicate entry, and invalid barcode scenarios.
- Updated `ISBN2Details` function to include fetching comprehensive book details from Google Books API.
- Improved code readability and structure by separating concerns into smaller methods for barcode decoding, book details fetching, UI updates, and sound handling.

### Fixed
- Fixed UI issue where clicking on a book entry in `book_list` did not update the details in `details_text` properly.
- Addressed potential bugs related to file handling and data serialization in `save_scanned_books` and `load_scanned_books` methods.
- Improved error handling for network requests (`requests.exceptions.RequestException`) and barcode decoding (`pyzbar` library).

## [3.7.0] - YYYY-MM-DD
### Added
- Introduced a "Toggle Dark Theme" button to switch between light and dark themes.
- Implemented `toggle_dark_theme` method to handle toggling between dark and light themes.
- Added `apply_theme` method to set stylesheet based on the current theme state (`dark_theme_enabled` flag).
- Included a default stylesheet in `apply_theme` for the light theme and updated it for the dark theme.

### Changed
- Updated the UI layout to include the "Toggle Dark Theme" button in the left layout alongside the video and status label.
- Refactored `apply_theme` method to change background and text colors based on the theme state.
- Adjusted stylesheet properties to improve readability and aesthetic appeal in both light and dark themes.

### Fixed
- Addressed potential UI inconsistencies related to theme switching by ensuring proper stylesheet application.
- Improved visual clarity and user experience by offering a choice between light and dark themes, enhancing accessibility.

## [3.8.0] - YYYY-MM-DD
### Added
- Added a "Toggle Camera" button to allow users to toggle the camera on and off.
- Implemented `toggle_camera` method to handle enabling and disabling the camera feed.
- Enhanced UI with dynamic updates to display current camera state (on/off) in the status label.
- Included error handling in `toggle_camera` method to manage exceptions related to camera initialization and release.

### Changed
- Updated the UI layout to incorporate the "Toggle Camera" button next to the "Toggle Dark Theme" button for easy access.
- Refactored `toggle_camera` method to manage camera state toggling and update status messages accordingly.
- Optimized camera initialization and release processes to improve application performance and stability.

### Fixed
- Addressed potential bugs related to camera initialization and release processes in `toggle_camera` method.
- Improved overall reliability and user experience by providing seamless camera toggling functionality.

## [4.0.0] - YYYY-MM-DD
### Added
- Introduced manual entry of ISBN numbers for scanning books without a barcode.
- Added support for scanning both ISBN-10 and ISBN-13 codes using the webcam.
- Integrated Google Books API to fetch book details based on ISBN for scanned books.
- Included functionality to display scanned book details in the application interface (`book_list` and `details_text`).
- Implemented saving scanned books to a CSV file (`scanned_books.csv`) for persistence.
- Added sound notifications for successful scans, errors, and status changes using `winsound` module.
- Implemented a dark theme toggle (`toggle_dark_theme`) for the application interface.
- Added a feature to toggle the camera on and off (`toggle_camera`).
- Included a feature to delete scanned books from the list (`delete_book`).

### Changed
- Refactored barcode scanning logic to handle different barcode types (ISBN-10 and ISBN-13).
- Improved UI layout to display scanned books (`book_list`) and process logs (`process_list`) efficiently.
- Enhanced error handling for network requests (`requests.exceptions.RequestException`) and barcode decoding (`pyzbar` library).

### Fixed
- Fixed bugs related to displaying incorrect book details for scanned ISBNs.
- Addressed UI inconsistencies and improved overall user experience.

## [4.1.0] - YYYY-MM-DD
### Added
- Implemented PyQt5 GUI components including QLabel, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout, QFrame, QListWidget, and QMessageBox for a user-friendly interface.
- Added real-time video feed from the webcam using OpenCV.
- Implemented a process list (`process_list`) to display real-time updates of scanned book entries.
- Enhanced user interaction by providing a visual list of scanned books and their titles (`book_list`).

### Changed
- Refactored the application structure to implement object-oriented programming (OOP) principles.
- Updated barcode processing to handle EAN-13 barcodes specifically for fetching book details.

### Fixed
- Fixed minor bugs related to text display and listbox updates in the GUI.
- Improved overall GUI responsiveness and layout management.

## [4.2.0] - YYYY-MM-DD
### Added
- Introduced a listbox in the GUI to display scanned ISBNs along with their corresponding titles (`book_list`).
- Implemented storage of full book details (including ISBN) for each scanned book in a list for future reference (`scanned_books`).

### Changed
- Adjusted GUI layout to include a listbox (`book_list`) for displaying scanned ISBNs and titles alongside book details.
- Enhanced user interaction by providing a visual list of scanned books and their titles.

### Fixed
- Fixed UI issue where clicking on a book entry in `book_list` did not update the details in `details_text` properly.
- Addressed potential bugs related to file handling and data serialization in `save_scanned_books` and `load_scanned_books` methods.

## [4.3.0] - YYYY-MM-DD
### Added
- Implemented manual entry of ISBN numbers.
- Added support for scanning ISBN-10 and ISBN-13 codes using the webcam.
- Integrated Google Books API to fetch book details based on ISBN for scanned books.
- Included functionality to display scanned book details in the application interface (`book_list` and `details_text`).
- Implemented saving scanned books to a CSV file (`scanned_books.csv`) for persistence.
- Added sound notifications for successful scans, errors, and status changes using `winsound` module.
- Implemented a dark theme toggle (`toggle_dark_theme`) for the application interface.
- Added a feature to toggle the camera on and off (`toggle_camera`).
- Included a feature to delete scanned books from the list (`delete_book`).

### Changed
- Refactored barcode scanning logic to handle different barcode types (ISBN-10 and ISBN-13).
- Improved UI layout to display scanned books (`book_list`) and process logs (`process_list`) efficiently.
- Enhanced error handling for network requests (`requests.exceptions.RequestException`) and barcode decoding (`pyzbar` library).

### Fixed
- Fixed bugs related to displaying incorrect book details for scanned ISBNs.
- Addressed UI inconsistencies and improved overall user experience.
