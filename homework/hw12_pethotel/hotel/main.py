from flask import request
from flask_restful import Resource

from . import db
from .models import Owner, Pet, Activities


class MainPage(Resource):
    def get(self):
        return {"message": "Welcome on main page"}, 200


class RoomPage(Resource):
    def get(self, room_id):
        settlers = Pet.query.filter_by(room_id=room_id).all()
        print(settlers)
        pets = {}
        for settler in settlers:
            pets[settler.name] = f'pet_id: {settler.id}, ' \
                                 f'owner: {settler.owner_info.name}, ' \
                                 f'settlement_date: {settler.settlement_date}'
        print(pets)
        if pets:
            return pets, 200
        else:
            return {'message': 'room is empty'}, 200


class SettlementPage(Resource):
    def post(self):
        from datetime import datetime

        response = request.get_json()
        name = response['name']
        phone_number = response['phone_number']
        pets = response['pets']
        room_id = response['room_id']

        user = Owner.query.filter_by(phone_number=phone_number).first()

        if user:
            return {"error": "phone number already exists"}, 404

        new_user = Owner(name=name, phone_number=phone_number)

        db.session.add(new_user)
        db.session.commit()

        cur_user = Owner.query.filter_by(name=name, phone_number=phone_number).first()

        for pet_name in pets:
            new_pet = Pet(name=pet_name,
                          owner_id=cur_user.id,
                          room_id=room_id,
                          settlement_date=datetime.now())

            db.session.add(new_pet)
            db.session.commit()

            cur_pet = Pet.query.filter_by(name=pet_name, owner_id=cur_user.id).first()

            for activity in pets[pet_name]:
                pet_activity = Activities(type=activity,
                                          time=pets[pet_name][activity],
                                          pet_id=cur_pet.id)

                db.session.add(pet_activity)
                db.session.commit()

        return {"status": "success"}, 200


class EvictionPage(Resource):
    def post(self):
        from datetime import date

        response = request.get_json()
        pet_names = response['pet_name']
        room_id = response['room_id']

        reply = {}

        for pet_name in pet_names:
            pet = Pet.query.filter_by(name=pet_name, room_id=room_id).first()
            owner_pets = Pet.query.filter_by(owner_id=pet.owner_info.id).all()
            pet_activities = Activities.query.filter_by(pet_id=pet.id).all()

            lived_days = (date.today() - pet.settlement_date).days

            db.session.delete(pet)
            for activity in pet_activities:
                db.session.delete(activity)
            db.session.commit()

            if not owner_pets:
                owner = Owner.query.filter_by(id=pet.owner_info.id).delete()
                db.session.delete(owner)
                db.session.commit()

            reply[pet_name] = {"lived_days_in_hotel": lived_days}

        return reply, 200


class ActivitiesPage(Resource):
    def get(self):
        information = {}
        activities_list = Activities.query.all()

        for activity in activities_list:
            if activity.time not in information:
                information[activity.time] = []
            information[activity.time].append({'pet_id': activity.pet_id, 'activity_type': activity.type})

        response = {}
        for key in sorted(information):
            response[key] = information[key]

        return response
