try {
    val resourceId = resources.getIdentifier("keukuk", "raw", packageName)
    val kukuPlayer = MediaPlayer.create(this, resourceId)

    kukuPlayer.start()
    delayWithMillis(1000)
    kukuPlayer.stop()
    kukuPlayer.release() // Release the MediaPlayer instance
    delayWithMillis(200)
} catch (e: Exception) {
    // Handle the exception here
}
