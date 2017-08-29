/***************************************************************************//**
  @file         main.c
  @author       Felix Foriel
  @date         Saturday, 26 August 2017
  @brief        FSH (F0RX SHell)
*******************************************************************************/

#include <sys/wait.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

/*
  Function Declarations for builtin shell commands:
 */
int fsh_cd(char **args);
int fsh_help(char **args);
int fsh_exit(char **args);

/*
  List of builtin commands, followed by their corresponding functions.
 */
char *builtin_str[] = {
  "cd",
  "help",
  "exit"
};

int (*builtin_func[]) (char **) = {
  &fsh_cd,
  &fsh_help,
  &fsh_exit
};

int fsh_num_builtins() {
  return sizeof(builtin_str) / sizeof(char *);
}

/*
  Builtin function implementations.
*/

/**
   @brief Bultin command: change directory.
   @param args List of args.  args[0] is "cd".  args[1] is the directory.
   @return Always returns 1, to continue executing.
 */
int fsh_cd(char **args)
{
  if (args[1] == NULL) {
    fprintf(stderr, "fsh: expected argument to \"cd\"\n");
  } else {
    if (chdir(args[1]) != 0) {
      perror("fsh");
    }
  }
  return 1;
}

/**
   @brief Builtin command: print help.
   @param args List of args.  Not examined.
   @return Always returns 1, to continue executing.
 */
int fsh_help(char **args)
{
  int i;
  printf("--- Felix Foriel's FSH ---\n");
  printf("Type program names and arguments, and hit enter.\n");
  printf("The following are built in:\n");

  for (i = 0; i < fsh_num_builtins(); i++) {
    printf("  %s\n", builtin_str[i]);
  }

  printf("Use the man command for information on other programs.\n");
  return 1;
}

/**
   @brief Builtin command: exit.
   @param args List of args.  Not examined.
   @return Always returns 0, to terminate execution.
 */
int fsh_exit(char **args)
{
  return 0;
}

/**
  @brief Launch a program and wait for it to terminate.
  @param args Null terminated list of arguments (including program).
  @return Always returns 1, to continue execution.
 */
int fsh_launch(char **args)
{
  pid_t pid;
  int status;

  pid = fork();
  if (pid == 0) {
    // Child process
    if (execvp(args[0], args) == -1) {
      perror("fsh");
    }
    exit(EXIT_FAILURE);
  } else if (pid < 0) {
    // Error forking
    perror("fsh");
  } else {
    // Parent process
    do {
      waitpid(pid, &status, WUNTRACED);
    } while (!WIFEXITED(status) && !WIFSIGNALED(status));
  }

  return 1;
}

/**
   @brief Execute shell built-in or launch program.
   @param args Null terminated list of arguments.
   @return 1 if the shell should continue running, 0 if it should terminate
 */
int fsh_execute(char **args)
{
  int i;

  if (args[0] == NULL) {
    // An empty command was entered.
    return 1;
  }

  for (i = 0; i < fsh_num_builtins(); i++) {
    if (strcmp(args[0], builtin_str[i]) == 0) {
      return (*builtin_func[i])(args);
    }
  }

  return fsh_launch(args);
}

#define FSH_RL_BUFSIZE 1024
/**
   @brief Read a line of input from stdin.
   @return The line from stdin.
 */
char *fsh_read_line(void)
{
  int bufsize = FSH_RL_BUFSIZE;
  int position = 0;
  char *buffer = malloc(sizeof(char) * bufsize);
  int c;

  if (!buffer) {
    fprintf(stderr, "fsh: allocation error\n");
    exit(EXIT_FAILURE);
  }

  while (1) {
    // Read a character
    c = getchar();

    if (c == EOF) {
      exit(EXIT_SUCCESS);
    } else if (c == '\n') {
      buffer[position] = '\0';
      return buffer;
    } else {
      buffer[position] = c;
    }
    position++;

    // If we have exceeded the buffer, reallocate.
    if (position >= bufsize) {
      bufsize += FSH_RL_BUFSIZE;
      buffer = realloc(buffer, bufsize);
      if (!buffer) {
        fprintf(stderr, "fsh: allocation error\n");
        exit(EXIT_FAILURE);
      }
    }
  }
}

#define FSH_TOK_BUFSIZE 64
#define FSH_TOK_DELIM " \t\r\n\a"
/**
   @brief Split a line into tokens (very naively).
   @param line The line.
   @return Null-terminated array of tokens.
 */
char **fsh_split_line(char *line)
{
  int bufsize = FSH_TOK_BUFSIZE, position = 0;
  char **tokens = malloc(bufsize * sizeof(char*));
  char *token, **tokens_backup;

  if (!tokens) {
    fprintf(stderr, "fsh: allocation error\n");
    exit(EXIT_FAILURE);
  }

  token = strtok(line, FSH_TOK_DELIM);
  while (token != NULL) {
    tokens[position] = token;
    position++;

    if (position >= bufsize) {
      bufsize += FSH_TOK_BUFSIZE;
      tokens_backup = tokens;
      tokens = realloc(tokens, bufsize * sizeof(char*));
      if (!tokens) {
		free(tokens_backup);
        fprintf(stderr, "fsh: allocation error\n");
        exit(EXIT_FAILURE);
      }
    }

    token = strtok(NULL, FSH_TOK_DELIM);
  }
  tokens[position] = NULL;
  return tokens;
}

/**
   @brief Loop getting input and executing it.
 */
void fsh_loop(void)
{
  char *line;
  char **args;
  int status;

  printf("+---------------------------------------------+-------------------------------------+\n");
  printf("| \033[31m##########   ######   #########  ####  ####\033[0m | F0RX 1.0 GNU/Linux Operating System |\n");
  printf("| \033[31m ##      #  ##    ##   ##     ##  ##    ## \033[0m +-------------------------------------+\n");
  printf("| \033[31m ##   #    ##    # ##  ##     ##   ##  ##  \033[0m | Welcome to F0RX GNU/Linux !         |\n");
  printf("| \033[31m ######    ##   #  ##  ########     ####   \033[0m |                                     |\n");
  printf("| \033[31m ##   #    ##  #   ##  ##   ##     ##  ##  \033[0m | Type intro for an overview of the   |\n");
  printf("| \033[31m ##         ###   ##   ##    ##   ##    ## \033[0m | base commands and type man for info |\n");
  printf("| \033[31m####         ######   ####  #### ####  ####\033[0m | on a specific command.              |\n");
  printf("|                                             |                                     |\n");
  printf("| \033[31m###########################################\033[0m | Enjoy !                             |\n");
  printf("+---------------------------------------------+-------------------------------------+\n");

  do {
    printf("? ");
    line = fsh_read_line();
    args = fsh_split_line(line);
    status = fsh_execute(args);

    free(line);
    free(args);
  } while (status);
}

/**
   @brief Main entry point.
   @param argc Argument count.
   @param argv Argument vector.
   @return status code
 */
int main(int argc, char **argv)
{
  // Load config files, if any.

  // Run command loop.
  fsh_loop();

  // Perform any shutdown/cleanup.

  return EXIT_SUCCESS;
}
