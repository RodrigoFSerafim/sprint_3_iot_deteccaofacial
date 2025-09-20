import cv2

# Haar cascades
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

olhos_fechados_frames = 0
limite_fechado = 45  # 1,5 segundos se 30fps

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detecta rostos
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(80, 80))

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        # Pega só a parte de cima do rosto (onde os olhos estão)
        roi_gray_upper = roi_gray[0:int(h/2), :]
        roi_color_upper = roi_color[0:int(h/2), :]

        # Detecta olhos apenas na metade superior
        eyes = eye_cascade.detectMultiScale(
            roi_gray_upper,
            scaleFactor=1.1,
            minNeighbors=10,
            minSize=(25, 25)
        )

        if len(eyes) == 0:
            olhos_fechados_frames += 1
        else:
            olhos_fechados_frames = 0

        # Alerta se olhos fechados por tempo demais
        if olhos_fechados_frames >= limite_fechado:
            cv2.putText(frame, "ATENCAO! OLHOS FECHADOS!", (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)

        # Desenha olhos detectados (na parte superior do rosto)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color_upper, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

    cv2.imshow("Detector de Atencao", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
