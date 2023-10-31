import constants


def main():
    user_age_str = input("Enter age:")

    try:
        int_user_age = int(user_age_str)
    except ValueError:
        print(f"{user_age_str} is not a valid age")
    else:
        if int_user_age < constants.MIN_AGE:
            print("You are to young to date my grandaughter")
        if int_user_age > constants.MAX_AGE:
            print("You are to old to date my grandaughter")
        elif int_user_age >= constants.MIN_AGE and int_user_age <= constants.MAX_AGE:
            print("you are just right for my grandchild")
    finally:
        print("thanks for telling me your age pretty boi")


if __name__ == "__main__":
    main()
