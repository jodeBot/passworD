def ok_password(password):
    ok_length = False
    cap_Letter = False
    small_Letter = False
    ok_number = False
    ok = False


    if len(password) >= 7:  #import minimum length for password, here 7
        ok_length = True
        for m in password:
            if m.isupper():
                cap_Letter = True
            if m.islower():
                small_Letter = True
            if m.isdigit():
                ok_number = True
        if cap_Letter and small_Letter and ok_number:
            ok = True
        else:
            ok = False

    return ok





