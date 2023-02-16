/*
    Use coroutines for delay operations

Instead of using Thread.sleep to add delays in the kukuSoundTimes and minutelyAlarms functions, it's recommended to use coroutines to avoid blocking the UI thread. You can use delay function from kotlinx.coroutines library.

    Replace Thread.sleep with delay in kukuSoundTimes

You can replace the call to Thread.sleep with delay function to avoid blocking the UI thread. Here's an example:
 */


 private suspend fun kukuSoundTimes(times: Int) {
    for (i in 1..times) {
        kukuSoundOnce()
        delay(1000)
    }
}


/*
Note that kukuSoundTimes needs to be marked with the suspend modifier to allow the delay function to be used.

    Use val instead of var when not reassigning variables

It's recommended to use val instead of var when not reassigning variables to avoid accidental modification of the variable. For example, the kukuScope variable can be declared using val as follows:
 */


 val kukuScope = MainScope()



/*
    Move UI-related code to the UI thread

Code that modifies the UI (e.g., resultTextView.text = "") should be executed on the UI thread to avoid concurrency issues. You can use runOnUiThread function to run code on the UI thread. Here's an example:
 */


runOnUiThread {
    resultTextView.text = ""
}


/*
    Simplify code using extension functions

You can use extension functions to simplify the code and make it more readable. For example, you can create an extension function on Calendar to format the time as a string. Here's an example:
 */



fun Calendar.formatTime(pattern: String): String {
    val formatter = SimpleDateFormat(pattern, Locale.getDefault())
    return formatter.format(time)
}


/*
Then you can use this function to format the current time as follows:
 */


val currentTime = Calendar.getInstance().formatTime("mm:ss")



/*
    Use in operator with ranges

Instead of using a loop to check if a value is within a range, you can use the in operator with ranges to simplify the code. For example, you can replace the following code in minutelyAlarms:

 */



 for (i in 0..59) {
    // ...
}

/*
with:
 */

 if (currentTime.substring(3) in (0..9).map { String.format("%02d", it) }) {
    // ...
}

/*
This checks if the seconds part of the current time is within the range of 00 to 09.

    Use setContentView with a view binding

You can use view binding to simplify the code for accessing views. Here's an example:
 */

 private lateinit var binding: ActivityMainBinding

override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    binding = ActivityMainBinding.inflate(layoutInflater)
    setContentView(binding.root)
}



/*

Then you can access views using binding.viewId.

I hope these suggestions are helpful for improving the provided Kotlin code!

 */


