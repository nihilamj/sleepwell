# Generate a random UUID
import uuid

def otp_generate():
    random_uuid = uuid.uuid4()
    print("Random UUID:", random_uuid)

    # Convert UUID to string
    uuid_string = str(random_uuid)
    print("UUID as String:", uuid_string)

    return uuid_string