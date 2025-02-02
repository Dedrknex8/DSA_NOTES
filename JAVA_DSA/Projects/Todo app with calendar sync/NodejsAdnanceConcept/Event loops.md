> The event loop is used to perform non blocking I/o operation in javascript.Like performing some task at a given time or run another task after a task is completed. Though javascript is single thread.

`timers -> pending callbakcs -> idle,prepare -> poll -> check -> close callbacks`
