import json

# To be moved
STAGE_ANSWERS = {
    1: "apple",
    2: "table",
    3: "cloud"
}

def lambda_handler(event, context):
    try:
        body = json.loads(event.get("body", "{}"))
        stage_id = body.get("stage_id")
        guess = body.get("guess", "").strip().lower()

        if not stage_id or stage_id not in STAGE_ANSWERS:
            return {"statusCode": 400, "body": json.dumps({"message": "Invalid stage ID"})}

        correct_word = STAGE_ANSWERS[stage_id]
        is_correct = guess == correct_word

        return {
            "statusCode": 200,
            "body": json.dumps({
                "correct": is_correct,
                "message": "Correct!" if is_correct else "Try again!"
            })
        }

    except Exception as e:
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}
