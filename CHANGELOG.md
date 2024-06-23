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
- Displays additional book details such as ISBN-13, ISBN-10, author, edition, binding, publisher, and published date.
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
- Improved overall user experience with real-time barcode scanning and dynamic updates.

### Changed
- Refactored the application structure to implement object-oriented programming (OOP) principles.
- Updated barcode processing to handle EAN-13 barcodes specifically for fetching book details.

### Fixed
- Fixed bugs related to displaying webcam feed and updating GUI elements dynamically.
- Improved error handling for API requests and book detail retrieval.

## [3.1.0] - YYYY-MM-DD
### Added
- Introduced a listbox in the GUI to display scanned ISBNs along with their corresponding titles.
- Implemented storage of full book details (including ISBN) for each scanned book in a list for future reference.

### Changed
- Adjusted GUI layout to include a listbox for displaying scanned ISBNs and titles alongside book details.
- Enhanced user interaction by providing a visual list of scanned books and their titles.

### Fixed
- Improved overall GUI responsiveness and layout management.
- Fixed minor bugs related to text display and listbox updates.

## [3.2.0] - YYYY-MM-DD
### Added
- Implemented saving scanned book details including timestamp to a CSV file (`scanned_books.csv`).
- Added a process box in the GUI to display real-time updates of scanned book entries.
- Implemented loading previously scanned books from the CSV file on application startup.

### Changed
- Enhanced user feedback with updated status messages displayed in the GUI.
- Optimized handling of duplicate barcode entries to notify the user when an entry already exists.

### Fixed
- Improved overall stability and performance of the application.
- Fixed minor bugs related to text display and CSV file handling.

## [3.3.0] - YYYY-MM-DD
### Added
- Implemented a PyQt5 GUI for the ISBN Scanner application.
- Added real-time video feed from the webcam using OpenCV.
- Added a process list to display real-time updates of scanned book entries.
- Implemented saving scanned book details including timestamp to a CSV file (`scanned_books.csv`).
- Added PyQt5 QMessageBox for displaying warnings when book details are not found or when an entry already exists.

### Changed
- Enhanced user interface with a more interactive and user-friendly layout using PyQt5 widgets (QLabel, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout, QFrame, QListWidget).
- Updated status messages displayed in the GUI for better user feedback during scanning and book details retrieval.

### Fixed
- Improved barcode decoding handling to catch and log errors more effectively.
- Fixed issues related to file handling for saving and loading scanned books data from `scanned_books.csv`.
- Enhanced overall application stability and performance.

## [3.4.0] - YYYY-MM-DD
### Added
- Implemented barcode decoding using `pyzbar` library with specific symbol set to `ZBarSymbol.EAN13`.
- Introduced error handling for barcode decoding errors to improve application stability.
- Added PyQt5 GUI components including QLabel, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout, QFrame, QListWidget, and QMessageBox for user interface and feedback.
- Enhanced user feedback with QMessageBox for displaying warnings when book details are not found or when an entry already exists.
- Added PyQt5 signals and slots to connect GUI elements with application logic.
- Improved status updates in the GUI to provide real-time feedback during barcode scanning and book details retrieval.

### Changed
- Updated barcode decoding mechanism to handle only EAN-13 barcodes, skipping non-EAN13 types.
- Optimized the layout of PyQt5 widgets for a more organized and user-friendly interface.
- Refactored barcode decoding function (`decode_barcodes`) to encapsulate barcode decoding logic and error handling.

### Fixed
- Fixed potential issues related to file handling for saving and loading scanned books data (`scanned_books.csv`).
- Enhanced overall application stability and performance with PyQt5-based GUI improvements and error handling.

## [3.5.0] - YYYY-MM-DD
### Added
- Enhanced book details retrieval by fetching additional information such as description, page count, categories, and language from Google Books API.
- Implemented PyQt5 GUI components including QLabel, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout, QFrame, QListWidget, and QMessageBox for a user-friendly interface.
- Incorporated error handling for network requests and barcode decoding to improve application stability.
- Added real-time feedback using QMessageBox for notifying users about invalid barcodes or duplicate entries.
- Expanded details shown in QTextEdit for scanned books to include description, page count, genre, and language.
- Introduced a new function `ISBN2Details` to handle fetching comprehensive book details from Google Books API.
- Implemented data persistence using CSV file (`scanned_books.csv`) for storing scanned book data including timestamp.

### Changed
- Updated barcode decoding to focus only on EAN-13 symbols using `pyzbar` library.
- Optimized layout and organization of PyQt5 widgets to improve usability and visual appeal.
- Refactored barcode scanning logic (`update_frame`) to handle different scenarios such as valid ISBN and existing entries efficiently.

### Fixed
- Addressed potential issues related to file handling and data serialization when saving and loading scanned books.
- Improved overall application performance and reliability through code refactoring and error handling enhancements.


## [3.6.0] - YYYY-MM-DD
### Added
- Implemented sound notifications using `winsound` module for different events: scan success, scan error, and status change.
- Added functionality to play beeping sounds on successful scan (`1000 Hz for 200 ms`), scan error (`500 Hz for 400 ms`), and status change (`800 Hz for 300 ms`).
- Introduced a wrapper method `play_sound` to handle different sound types based on specific events in the application.
- Implemented functionality to display details of a selected book from the list by clicking on its entry in `book_list`.
- Enhanced user interface by displaying detailed book information in `details_text` when a book entry is clicked in `book_list`.
- Updated PyQt5 signal connection (`itemClicked`) to trigger the display of book details on list item click.

### Changed
- Modified the `show_book_details` method to append book details to `details_text` and also add the scanned book to `process_list` for tracking scanned items.
- Refactored `update_frame` method to include sound notifications on successful scan, duplicate entry, and invalid barcode scenarios.
- Updated `ISBN2Details` function to include fetching additional book information such as description, page count, categories, and language from Google Books API.
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
- Enhanced UI by providing users the option to switch between light and dark themes dynamically.
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
- Implemented `toggle_camera` method to handle toggling the camera state.
- Introduced `show_camera_off_icon` method to display a camera-off icon when the camera is turned off.
- Incorporated `camera_on` flag to track the current camera state (`True` for on, `False` for off).
- Enhanced UI by providing users the option to turn the camera on or off dynamically.

### Changed
- Updated the UI layout to include the "Toggle Camera" button in the left layout alongside the video and status label.
- Adjusted `update_frame` method to check `self.camera_on` flag before reading frames from the camera.
- Refactored camera-related methods to ensure proper camera initialization and release.

### Fixed
- Addressed potential issues related to camera handling to improve reliability and user experience.
- Optimized camera controls to prevent resource leaks and ensure smooth operation.



## [4.0.0] - YYYY-MM-DD

### Added Features:
#### ISBN Type Selection:

- Added a dropdown (QComboBox) to select between "ISBN-10" and "ISBN-13" types for entering ISBN.
Depending on the length of the entered ISBN, automatically switches between "ISBN-10" and "ISBN-13".
ISBN Input Validation:

- Validates the length of the entered ISBN based on the selected type ("ISBN-10" or "ISBN-13").
Displays error messages and flashes status indicators for invalid ISBN lengths.
ISBN Adding Functionality:

- Introduced an "Add" button that triggers fetching book details upon entering a valid ISBN.
Displays fetched book details in the UI upon successful retrieval.
Supports addition of books to the scanned books list with timestamp.

### UI/UX Improvements:
#### Enhanced Dark Theme:

- Implemented a toggle button to switch between dark and light themes.
Improved styling for better readability and user experience in dark mode.
Camera Toggle Functionality:

- Added functionality to toggle the camera on/off using a dedicated button (toggle_camera_button).
Displays a camera-off icon (camera_off.png) when the camera is turned off.
Bug Fixes and Enhancements:
Improved Status Updates:

- Enhanced status updates to provide more informative messages for various actions (e.g., scan success, errors, entry already exists).
Error Handling:

- Implemented error handling improvements for barcode decoding errors and network errors when fetching book details.
Data Persistence:

- Updated file paths for saving and loading scanned books data (scanned_books.csv located in assets/data/).

### Code Organization:
#### Modularized Layout Management:

- Improved layout management by organizing UI elements into separate layouts (left_layout, right_layout, button_layout, etc.) for better readability and maintainability.
Refactored Code Structure:

- Restructured code to enhance readability and maintainability, including modularizing functions and separating concerns.

## Version 4.1.0 Release Notes

### New Features

- **Dark Mode Toggle**
  - Added a button to toggle between light and dark themes for the application UI.
  - Users can now switch to a dark background with white text for better readability in low-light environments.

- **Camera Toggle**
  - Implemented a button to toggle the camera feed on and off.
  - Allows users to disable the camera when not scanning, conserving resources and preventing unintended captures.

- **Dynamic ISBN Input Validation**
  - Improved ISBN input validation based on the selected ISBN type (ISBN-10 or ISBN-13).
  - Provides immediate feedback on input length validity before attempting to fetch book details.

- **Error Handling and Status Updates**
  - Enhanced error messages and status updates displayed to the user interface.
  - Alerts users about invalid ISBNs, existing entries, and errors encountered during book data retrieval.

- **Sound Feedback**
  - Added sound notifications for successful scans, errors, and status changes.
  - Enhances user experience by providing audible confirmation of actions taken.

- **Book Details Display**
  - Expanded book details display with additional information:
    - Publisher
    - Published Date (Edition)
    - Description
    - Page Count
    - Genre
    - Language

- **Persistent Data Storage**
  - Implemented CSV file storage for scanned books data.
  - Enables persistence across application restarts, maintaining a history of scanned ISBNs and associated book details.

- **User Interface Improvements**
  - Enhanced layout and alignment for better usability.
  - Improved clarity and organization of controls, lists, and status indicators.

### Bug Fixes

- **Camera Initialization**
  - Fixed issues related to camera initialization and release.
  - Ensures proper handling of camera resources to prevent crashes and errors.

- **Barcode Detection**
  - Improved barcode detection accuracy and handling.
  - Ensures consistent recognition and processing of valid EAN-13 barcodes.

### Known Issues

- **Camera Stability**
  - Occasional instability when toggling the camera on and off repeatedly.
  - Ongoing investigation and improvements planned for future updates.

### Developer Notes

- **Code Optimization**
  - Refactored code for improved readability and maintainability.
  - Implemented best practices for PyQt5 application development.

- **Dependencies**
  - Updated dependencies to latest stable versions.
  - Ensures compatibility and security updates.
 
  
## Version 4.2.0

### Added
- Implemented manual entry of ISBN numbers.
- Added support for scanning ISBN-10 and ISBN-13 codes.
- Integrated Google Books API to fetch book details based on ISBN.
- Included functionality to display scanned book details in the application.
- Implemented saving scanned books to a CSV file for persistence.
- Added sound notifications for successful scans, errors, and status changes.
- Implemented a dark theme toggle for the application interface.
- Added a feature to toggle the camera on and off.
- Included a feature to delete scanned books from the list.

### Changed
- Refactored barcode scanning logic to handle different barcode types.
- Improved UI layout to display scanned books and process logs more efficiently.
- Enhanced error handling for network requests and barcode decoding errors.

### Fixed
- Fixed bugs related to displaying incorrect book details for scanned ISBNs.
- Fixed issues with handling edge cases for invalid ISBNs and network errors.
- Addressed UI inconsistencies and improved overall user experience.


## Version 4.3.0

### Refactored Book Details Handling:
- Enhanced error handling in `get_book_details()` function when fetching book details from Google Books API.
- Improved validation for ISBN-13 identification and retrieval.

### UI Enhancements:
- Introduced a dark theme toggle button (`toggle_dark_theme_button`) to switch between light and dark themes.
- Improved camera toggle functionality (`toggle_camera_button`) for turning the camera on/off.
- Integrated `status_label` to display status messages with color coding for different states (e.g., success, warning, error).

### Manual ISBN Entry:
- Added manual entry of ISBNs via `isbn_input` (`QLineEdit`) and `add_button` (`QPushButton`) for adding books manually.
- Introduced `isbn_type_dropdown` (`QComboBox`) to select between ISBN-10 and ISBN-13 formats.

### Barcode Scanning:
- Implemented barcode scanning using OpenCV (`cv2`) and `pyzbar` library for decoding EAN-13 barcodes.
- Displayed scanned book details in `details_text` (`QTextEdit`) and updated lists (`book_list`, `process_list`).

### Data Persistence:
- Improved saving and loading of scanned books using CSV files (`scanned_books.csv`).
- Added `save_scanned_books()` and `load_scanned_books()` methods for managing scanned books' data across sessions.

### User Feedback:
- Enhanced user feedback with status updates (`update_status()`) displayed in `status_label`.
- Implemented sound notifications (`play_sound()`) for different events (scan success, scan error, status change) using `winsound`.

### UI Layout and Components:
- Organized UI components into `QVBoxLayout` and `QHBoxLayout` layouts for better structure and clarity.
- Included buttons (`delete_button`, `quit_button`) for deleting selected books and quitting the application, respectively.

### Error Handling and Logging:
- Improved error handling for network requests (`requests.exceptions.RequestException`) and barcode decoding errors (`Exception`).

