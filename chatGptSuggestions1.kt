/*
ViewBinding
Avoid using findViewById() repeatedly in the code. Instead, use data binding or ViewBinding to bind views to Kotlin classes.
*/

/*
MediaPlayer
Add a try-catch block around the MediaPlayer.create() call in kukuSoundOnce() and handle any exceptions that may occur.
*/

/*
Sealed classes.
The quarters array in the quarterlyAlarms() function contains a fixed set of values. To make this more explicit, it can be defined as a sealed class with a fixed set of subclasses.
 */
    private sealed class Quarter(val time: String) {
        object Quarter15 : Quarter("15:00")
        object Quarter30 : Quarter("30:00")
        object Quarter45 : Quarter("45:00")
    }

    private suspend fun quarterlyAlarms() {
        val getCurrentTime = Calendar.getInstance().time
        val formatter = SimpleDateFormat("mm:ss", Locale.getDefault())
        val currentTime = formatter.format(getCurrentTime)

        when (currentTime) {
            Quarter.Quarter15.time -> kukuAlert(true, true)
            Quarter.Quarter30.time -> kukuAlert(true, true)
            Quarter.Quarter45.time -> kukuAlert(true, true)
        }
    }


/* 
Combine Sound and Text
*/
private fun kukuAlert(playSound: Boolean, showText: Boolean) {
        if (playSound) {
            val resourceId = resources.getIdentifier("keukuk", "raw", packageName)
            val kukuPlayer = MediaPlayer.create(this, resourceId)
            kukuPlayer.start()
        }

        if (showText) {
            val kukuToast = Toast.makeText(applicationContext,
                getString(R.string.kukukTextView),
                Toast.LENGTH_LONG)

            kukuToast.show()
        }
    }


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
*/
