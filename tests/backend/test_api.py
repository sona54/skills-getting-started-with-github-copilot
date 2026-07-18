from urllib.parse import quote


def test_signup_for_activity_adds_participant(client):
    # Arrange
    activity_name = "Chess Club"
    email = "backend-test@mergington.edu"
    activity_path = quote(activity_name, safe="")

    # Act
    response = client.post(f"/activities/{activity_path}/signup?email={email}")
    activities_response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    assert response.json() == {"message": f"Signed up {email} for {activity_name}"}
    assert email in activities_response.json()[activity_name]["participants"]


def test_unregister_participant_removes_email_from_activity(client):
    # Arrange
    activity_name = "Chess Club"
    email = "backend-delete-test@mergington.edu"
    activity_path = quote(activity_name, safe="")
    signup_response = client.post(f"/activities/{activity_path}/signup?email={email}")
    assert signup_response.status_code == 200

    # Act
    unregister_response = client.delete(
        f"/activities/{activity_path}/participants/{quote(email, safe='')}"
    )
    activities_response = client.get("/activities")

    # Assert
    assert unregister_response.status_code == 200
    assert email not in activities_response.json()[activity_name]["participants"]
