import pickle
import os
import config

model_folder_path = config.MODEL_FOLDER_PATH
if not os.path.exists(model_folder_path):
    os.mkdir(model_folder_path)

def predct_satisfaction(Gender, Customer_Type, Age, Type_of_Travel, Class,
       Flight_Distance, Inflight_wifi_service, Ease_of_Online_booking,
       Food_and_drink, Online_boarding, Seat_comfort,
       Inflight_entertainment, On_board_service, Leg_room_service,
       Baggage_handling, Checkin_service, Inflight_service,
       Cleanliness):
    
    RF_model = pickle.load(open(f'{model_folder_path}/model.pkl','rb'))
    print('RF_model: ',RF_model)
    
    pred1 = RF_model.predict([[Gender, Customer_Type, Age, Type_of_Travel, Class,
       Flight_Distance, Inflight_wifi_service, Ease_of_Online_booking,
       Food_and_drink, Online_boarding, Seat_comfort,
       Inflight_entertainment, On_board_service, Leg_room_service,
       Baggage_handling, Checkin_service, Inflight_service,
       Cleanliness]])
    prediction1 = pred1[0]
    print("Predicted output is :",prediction1)
    return prediction1

predct_satisfaction(1,0,3.8,0,1,37.0,1,1,4,1,1,4,1,1,3,2,3,4)