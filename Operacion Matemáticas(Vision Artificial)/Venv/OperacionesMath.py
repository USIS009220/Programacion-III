import cv2
import SeguimientoManos as sn

detector = sn.detectormanos(Confdeteccion=0.75)

cap = cv2.VideoCapture(1)

d1 = 0
d2 = 0
r = 0
cx= 65
cy = 420
comp = 0
res = 0


while True:
    ret, frame = cap.read()

    frame = detector.encontrarmanos(frame)

    cv2.rectangle(frame, (50, 50), ( 130, 150), (0, 0, 0), cv2.FILLED)

    cv2.rectangle(frame, (50, 350), ( 130, 450), (0, 0, 0), cv2.FILLED)

    cv2.rectangle(frame, (50, 350), ( 330, 450), (0, 0, 0), cv2.FILLED)

    cv2.rectangle(frame, (450, 350), ( 600, 450), (0, 0, 0), cv2.FILLED)

    cv2.putText(frame, "Dedos", (52, 145), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)

    cv2.putText(frame, "Digito 1", (45, 445), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)
    cv2.putText(frame, str(d1), (65, 420), cv2.FONT_HERSHEY_PLAIN, 5, (0, 255, 0), 10)

    cv2.putText(frame, "Digito 2", (245, 445), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)
    cv2.putText(frame, str(d1), (265, 420), cv2.FONT_HERSHEY_PLAIN, 5, (0, 255, 0), 10)

    cv2.putText(frame, "Resultado", (465, 445), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)
    cv2.putText(frame, str(d1), (495, 420), cv2.FONT_HERSHEY_PLAIN, 5, (0, 255, 0), 10)

    manosInfo, cuadro = detector.encontrarposicion(frame, dibujar=False)

    if len(manosInfo) != 0:
        dedos = detector.dedosarriba()
        print(dedos)
        contar = dedos.count(1)
        cv2.putText(frame, str(contar), (65, 125), cv2.FONT_HERSHEY_PLAIN, 5, (0, 255, 0), 10)

        #Suma
        if t == 83 or t == 115:
            comp = 1
            d1 = contar
        #Mostrar suma
        if comp == 1:
            cv2.putText(frame, str(d1), (65, 420), cv2.FONT_HERSHEY_PLAIN, 5, (0, 255, 0), 10)
            cv2.putText(frame, "+", (165, cy), cv2.FONT_HERSHEY_PLAIN, 5, (0, 255, 0), 10)

        #Respuesta
        if t == 32:
            d2 = contar
            res = 1
