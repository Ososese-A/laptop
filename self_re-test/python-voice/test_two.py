import speech_recognition as sr
import pyttsx3

#Initialize recognizer which is the object that ineracts with the microphone
r = sr.Recognizer()

def record_text():
    #loop incase of errors 
    while(1):
        try:
            with sr.Microphone() as source2:

                r.adjust_for_ambient_noise(source2,duration=0.2)

                audio2 = r.listen(source2)

                myText = r.recognize_google_cloud(audio2)



        except sr.RequestError as e:
            print("Could not request; {0}".format(e))

        except sr.UnknownValueError:
            print("Unknown error occured")
    
    return

def output_text(text):

    f = open("output.txt","a")
    f.write(text)
    f.write("\n")
    f.close()
    return

while(1):
    text = record_text()
    output_text(text)

    print("Wrote text")