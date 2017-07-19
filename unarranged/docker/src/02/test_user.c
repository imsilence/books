#define _GNU_SOURCE
#include <sys/types.h>
#include <sys/wait.h>
#include <sys/capability.h>
#include <stdio.h>
#include <sched.h>
#include <signal.h>
#include <unistd.h>

#define STACK_SIZE (1024 * 1024)
#define PATH_SIZE 1024

static char child_stack[STACK_SIZE];

char* const child_args[] = {
    "/bin/bash",
    NULL
};

int set_map(pid_t pid, char* map_type, int inside_id, int outside_id, int length) {
    char path[PATH_SIZE];
    sprintf(path, "/proc/%d/%s", getpid(), map_type);
    printf("%s %d %d %d\n", path, inside_id, outside_id, length);
    FILE* handler = fopen(path, "w");
    fprintf(handler, "%d %d %d", inside_id, outside_id, length);
    fclose(handler);
    return 0;
}

int child_main(void* args) {
    printf("子进程启动\n");
    set_map(getpid(), "gid_map", 0, 1000, 1);
    set_map(getpid(), "uid_map", 0, 1000, 1);
    cap_t caps;
    printf("eUID=%d, eGID=%d\n", geteuid(), getegid());
    caps = cap_get_proc();
    printf("capabilities:%s\n", cap_to_text(caps, NULL));
    execv(child_args[0], child_args);
    return 1;
}

int main(int argc, char** argv) {
    printf("父进程启动\n");
    int child_pid = clone(child_main, child_stack + STACK_SIZE, CLONE_NEWUSER | SIGCHLD, NULL);
    //int child_pid = clone(child_main, child_stack + STACK_SIZE, CLONE_NEWUSER | CLONE_NEWNS | CLONE_NEWPID | CLONE_NEWIPC | CLONE_NEWUTS | SIGCHLD, NULL);
    waitpid(child_pid, NULL, 0);
    printf("父进程结束\n");
    return 0;
}