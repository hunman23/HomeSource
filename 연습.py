import win32com.client
import win32api
shell = win32com.client.Dispatch("WScript.Shell")
shell.Run("calc")
win32api.Sleep(100)
shell.AppActivate("Calculator")
win32api.Sleep(100)
shell.SendKeys("1{+}")
win32api.Sleep(500)
shell.SendKeys("2")
win32api.Sleep(500)