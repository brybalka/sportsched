from datetime import datetime
from flask import Flask
from flask_restful import Api, Resource, reqparse
from crud import get_ufc_events

app = Flask(__name__)
api = Api(app)


class UFCEvent(Resource):
    get_parser = reqparse.RequestParser()
    get_parser.add_argument('fighters', action='append', location='args')
    get_parser.add_argument('start_date', type=lambda x: datetime.strptime(x, '%m/%d/%Y'), location='args')
    get_parser.add_argument('limit', type=int, location='args')

    def get(self):
        args = self.get_parser.parse_args()
        ufc_events = get_ufc_events(args['start_date'], args['fighters'], limit=args['limit'])
        data = [{'id': ev.id, 'name': ev.name, 'date': ev.date.strftime('%m/%d/%Y'), 'status': ev.status} for ev in
                ufc_events]
        return data


api.add_resource(UFCEvent, '/ufc/event')

if __name__ == '__main__':
    app.run(debug=True)
