import cv2
import webbrowser

cap = cv2.VideoCapture(0)

# Initialize the QR Code detector
detector = cv2.QRCodeDetector()

while True:
    _, img = cap.read()
    
    # Detect and decode the QR code
    data, bbox, _ = detector.detectAndDecode(img)
    
    if bbox is not None:
        # Display the image with the bounding box
        for i in range(len(bbox)):
            cv2.line(img, tuple(bbox[i][0]), tuple(bbox[(i+1) % len(bbox)][0]), color=(255, 0, 0), thickness=2)
        if data:
            print("QR Code detected--->", data)
            webbrowser.open(data)  # Open the URL in a browser
            break

    # Display the result
    cv2.imshow("QR Code Scanner", img)    
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
