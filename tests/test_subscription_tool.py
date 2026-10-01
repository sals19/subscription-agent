from app.tools.subscription_tools import get_my_subscription


def test_get_my_subscription():

    user_id = "a7c145f2293f4c9b844f2c862ed62d28"

    result = get_my_subscription.invoke({
        "user_id": user_id
    })

    print("\nRESULT:")
    print(result)

    assert result is not None