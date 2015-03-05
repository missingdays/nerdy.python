#include <stdio.h>
#include <conio.h>

int main(void)
{
    char kl;

    while (kl!=27)
    {
        kl=getch();
        switch(kl)
        {
        case -32: kl=getch();
            switch(kl)
            {
            case 83: printf("DEL\n");
                break;
            case 82: printf("INSERT\n");
                break;
            case 79: printf("END\n");
                break;
            case 71: printf("HOME\n");
                break;
            case 81: printf("PAGE DOWN\n");
                break;
            case 73: printf("PAGE UP\n");
                break;
            case 72: printf("UP\n");
                break;
            case 80: printf("DOWN\n");
                break;
            case 75: printf("LEFT\n");
                break;
            case 77: printf("RIGHT\n");
                break;
            default: printf("%c\n", kl);
                break;
            }
            break;
        case 0: kl=getch();
            switch(kl)
            {
            case 59: printf("F1\n");
                break;
            case 60: printf("F2\n");
                break;
            case 61: printf("F3\n");
                break;
            case 62: printf("F4\n");
                break;
            case 63: printf("F5\n");
                break;
            case 64: printf("F6\n");
                break;
            case 65: printf("F7\n");
                break;
            case 66: printf("F8\n");
                break;
            case 67: printf("F9\n");
                break;
            case 68: printf("F10\n");
                break;
            case 80: printf("DOWN\n");
                break;
            case 75: printf("LEFT\n");
                break;
            case 77: printf("RIGHT\n");
                break;
            case 72: printf("UP\n");
                break;
            case 83: printf("DEL\n");
                break;
            case 82: printf("INSERT\n");
                break;
            case 79: printf("END\n");
                break;
            case 71: printf("HOME\n");
                break;
            case 81: printf("PAGE DOWN\n");
                break;
            case 73: printf("PAGE UP\n");
                break;
            default: printf("");
                break;
            }
            break;
        case -123: printf("F11\n");
            break;
        case -122: printf("F12\n");
            break;
        case 13: printf("ENTER\n");
            break;
        case 8: printf("BACKSPACE\n");
            break;
        case 9: printf("TAB\n");
            break;
        case 32: printf("SPACE\n");
            break;
        default: printf("%c\n", kl);
            break;
        }

    }
    return 0;
}

