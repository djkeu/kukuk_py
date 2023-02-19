1    ViewBinding
Avoid using findViewById() repeatedly in the code. Instead, use data binding or ViewBinding to bind views to Kotlin classes.


2    Move UI-related code to the UI thread
Code that modifies the UI (e.g., resultTextView.text = "") should be executed on the UI thread to avoid concurrency issues. You can use runOnUiThread function to run code on the UI thread. Here's an example:


runOnUiThread {
    resultTextView.text = ""
}


3   Use setContentView with a view binding
You can use view binding to simplify the code for accessing views. Here's an example:


private lateinit var binding: ActivityMainBinding

override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    binding = ActivityMainBinding.inflate(layoutInflater)
    setContentView(binding.root)
}

Then you can access views using binding.viewId.
