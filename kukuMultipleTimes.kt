    // Show kuku text multiple times
    /*
    @Suppress("unused")
    private fun kukuTextTimes(times: Int) {
        // Moved to kukuSoundTimes
        for (i in 1..times) {
            kukuTextOnce()
        }
    }
    */


    // Play kuku sound multiple times
    private suspend fun kukuSoundTimes(times: Int) {
        for (i in 1..times) {
            kukuTextOnce()
            kukuSoundOnce()
        }
    }


