import cv2
import numpy as np
from pyzbar.pyzbar import decode

def main():
    # Initialize the webcam
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        # Decode the barcodes in the frame
        barcodes = decode(frame)

        for barcode in barcodes:
            # Extract the bounding box location of the barcode and draw it
            (x, y, w, h) = barcode.rect
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Extract the barcode data
            barcode_data = barcode.data.decode('utf-8')
            barcode_type = barcode.type

            # Display the barcode data and type on the frame
            text = f"{barcode_data} ({barcode_type})"
            cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            # Print the barcode data to the console
            print(f"Decoded {barcode_type}: {barcode_data}")

        # Display the resulting frame
        cv2.imshow('Barcode/ISBN Scanner', frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture and close the windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
