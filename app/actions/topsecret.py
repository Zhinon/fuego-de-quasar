from app.actions.base import BaseAction

class GetCoordsAndMessageAction(BaseAction):

    def validate(self, request):
        pass

    def _run(self, request):
        return {
            'position': { 'x': 10, 'y': 11},
            'message': 'Este es un mensaje',
        }