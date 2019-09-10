#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <errno.h>

sigset_t mSignalSet;

int BlockSignal() {
    if (sigprocmask(SIG_BLOCK, &mSignalSet, NULL) == -1) {
        printf("Failed to block signal!\n");
    }

    return 1;
}

int UnblockSignal() {
    if (sigprocmask(SIG_UNBLOCK, &mSignalSet, NULL) == -1) {
        printf("Failed to unblock signal!\n");
    }

    return 1;
}

int main(int argc, char** args)
{
    if ((sigemptyset(&mSignalSet) == -1) || (sigaddset(&mSignalSet, SIGSEGV) == -1)) {
        printf("Failed to add SIGSEGV\n");
        return 1;
    }

    // cout << "Block signal" << endl;
    printf("SignalSet: %d\n", mSignalSet);
    BlockSignal();
    printf("SignalSet: %d\n", mSignalSet);

    sleep(2);

    char* a = NULL;
    a[1] = 'a';

    // cout << "Unblock signal" << endl;

    UnblockSignal();

    while(1){
        sleep(1);
    }

    return 1;
}
