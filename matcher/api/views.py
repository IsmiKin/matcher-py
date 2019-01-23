
# IDEA: Usually it would be a structure like follows:
# - entity
#    - views.py (endpoints)
#    - logic.py (logic to do for each endpoint)
#    - data.py  (methods to retrieve entities / data)
#
# But this case due the relation between entities are so tight
# and the size it's too small it would be simplify in just one structure

from flask import Blueprint, request

from .util import generate_response, handle_errors
from .logic import process_file as process_new_file


process_file = Blueprint('process_file', __name__)


@process_file.route('/v1/process_file/', methods=['POST'])
@handle_errors
def process_file_endpoint():
    """
    Process a file
    """
    params = request.get_json()

    payload = process_new_file(
        'pika'
    )

    return generate_response(payload)
