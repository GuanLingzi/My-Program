#include <windows.h>

BOOL CALLBACK EnumWindowsProc(HWND hwnd,LPARAM IParam)
{
    PostMessage(hwnd, WM_CLOSE, 0, 0);
	return TRUE;
}

int APIENTRY WinMain(HINSTANCE hInstance,
                     HINSTANCE hPrevInstance,
                     LPSTR     lpCmdLine,
                     int       nCmdShow)
{
	EnumWindows(EnumWindowsProc,0);
	return 0;
}

