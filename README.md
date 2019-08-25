# WeChat Group Messages Monitor

> Too many WeChat groups? And just some of the messages are important to you?
>
> Let's use \[wxpy] to write a little tool...

## `QuestionMonitor`

class `QuestionMonitor` provides main function.

After getting an instance, use `setGroups()` and `setContents()` to set which groups and what messages you want.

For example, `setGroups(['a', 'b'])` will monitor all groups whose name contain `'a'` or `'b'`. And `setContents(['c', 'd'])` will captures all messages which contain `'a'` or `'b'`.

After captured a message, the monitor will send an email. **So you need to config your email in `_capturedContent()` before you run the code.**