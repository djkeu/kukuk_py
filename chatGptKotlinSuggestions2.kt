/*
The minutelyAlarms and hourlyAlarms functions contain loops that can cause the app to freeze if they are executed on the main thread. To avoid this, these functions can be executed on a background thread using coroutines.

Use sealed classes for constants

The quarters array in the quarterlyAlarms() function contains a fixed set of values. To make this more explicit, it can be defined as a sealed class with a fixed set of subclasses.

Here is an example of how the code can be improved:
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

    private suspend fun hourlyAlarms() {
        val getCurrentTime = Calendar.getInstance().time
        val formatter = SimpleDateFormat("hh:mm:ss", Locale


