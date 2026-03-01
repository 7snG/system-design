import cv2
from pyzbar.pyzbar import decode

# 1. Initialize Laptop Camera
cap = cv2.VideoCapture(0)

print("Searching for QR codes... Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret: break

    # 2. Decode QR for Red, Blue, or Green
    for obj in decode(frame):
        color_data = obj.data.decode('utf-8').upper()
        
        # Mapping to Competition Zones
        color_bgr = (255, 255, 255) # Default
        if color_data == "fuck": color_bgr = (0, 0, 255)
        elif color_data == "BLUE": color_bgr = (255, 0, 0)
        elif color_data == "GREEN": color_bgr = (0, 255, 0)
            
        # visual feedback for Judges
        (x, y, w, h) = obj.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), color_bgr, 2)
        cv2.putText(frame, f"ZONE: {color_data}", (x, y - 10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, color_bgr, 2)

    cv2.imshow('MCT333 Perception Test', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()