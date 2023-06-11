from flask import Flask,request,jsonify
import utils

app = Flask(__name__)
@app.route("/prediction",methods = ['POST'])

def prediction():
    print("prediction API")
    data = request.form
    if request.method == 'POST':
        print("Input data is ",data)
        x1 = float(data['Gender'])
        x2 = float(data['Customer_Type'])
        x3 = float(data['Age'])
        x4 = float(data['Type_of_Travel'])
        x5 = float(data['Class'])
        x6 = float(data['Flight_Distance'])
        x7 = float(data['Inflight_wifi_service'])
        x8 = float(data['Ease_of_Online_booking'])
        x9 = float(data['Food_and_drink'])
        x10 = float(data['Online_boarding'])
        x11= float(data['Seat_comfort'])
        x12= float(data['Inflight_entertainment'])
        x13 = float(data['On_board_service'])
        x14 = float(data['Leg_room_service'])
        x15 = float(data['Baggage_handling'])
        x16 = float(data['Checkin_service'])
        x17 = float(data['Inflight_service'])
        x18 = float(data['Cleanliness']) 

        predictions = utils.predct_satisfaction(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18)

        return f"prediction is {predictions}"
    
    else:
        return "Model fail"

if __name__ == "__main__":
    app.run(debug=True)