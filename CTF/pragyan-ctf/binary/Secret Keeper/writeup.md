# Secret Keeper:

## Program notes:
### User structure:
```
typedef struct _user{
    char *username_;
    char *password_;
    char secret_info_[0x32];
} User;
```

Notes:
* Both username and password point to a buffer of size 0x14 bytes.
*
* The User structure is 0x48 bytes.

### Global variables:
* The number of objects is stored as a 32-bit integer at 0x0020202c.
* The array of users starts at address 0x202040.
* When a new user is created, the User object is inserted at the end of the
array.

### Operations:
1. Register:
* The user enters their username + password. Both the username and the password,
must each be less than 0x13 bytes.
* Program allocates a User object and copies the username + password into the
object.
* **Password is allocated first**
* The program then increments the global count of users and then inserts the
User object into the end of a global array of users.

2. Login:
* After the user has logged in they can:
    - Enter a secret message of size 0x32
    - View their secret message
    - Delete their user

* If the username is admin, then the password check is performed against the
contents of a file called password.txt.
* Deleting the user doesn't seem to actually delete the user but only deletes
the username.

## Vulnerability:
* This is a use after free vulnerability.

## Exploit idea:
* The delete user only frees the username of the user not the user object.
* Also, since the password is allocated first, maybe we can inject "admin"
into the username of the "freed" user.

## Steps to exploit:
1. Create a user with username: aaaabbbb and password: ccccdddd.
2. Login as aaaabbbb:ccccdddd and delete the user.
    At this point, the pointer to the username: aaaabbbb will be freed and will
    be in one of the fastbins.
3. Create a new user with username: whatever and password: admin
    The pointer in the fastbin is given to this user to store the password.

    The username of the "freed" user and the password of the new user both
    point to the same memory. This memory now contains "admin". We have
    indirectly changed the username of the first user.

4. Login as username: admin and password: ccccdddd and the flag should be shown.
