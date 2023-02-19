Use when statement instead of long if..else ladder:

As the TODO suggests, it is better to use a when statement instead of a long if-else ladder. This makes the code more concise and easier to read. Here's an example:

val times = when {
    i == 0 -> 10
    i < 11 -> i - 0
    i < 21 -> i - 10
    i < 31 -> i - 20
    i < 41 -> i - 30
    i < 51 -> i - 40
    else -> i - 50
}


Use Kotlin's built-in date/time APIs:

Instead of using Date and SimpleDateFormat from the Java API, it is recommended to use Kotlin's built-in date/time APIs. Here's an example:


val currentTime = LocalTime.now()
val minute = currentTime.format(DateTimeFormatter.ofPattern("mm:ss"))


Use a more meaningful name for the function:

The name minutelyAlarms() is not very clear about what the function does. It would be better to use a more meaningful name that describes the purpose of the function.


Consider using coroutines for asynchronous programming:

Since the function is already marked with the suspend modifier, it is likely that it is part of an asynchronous program. In that case, it may be useful to use coroutines to make the code more concise and easier to reason about.


