<h1>simple html page</h1>
<h2>no ui is required</h2>

<!--honeypot 1 :ip blocker -->
<!-- so basically this a hidden link points to a uri not accessible by normal users -->
<!-- only bots can find this link -->
<!-- if the uri is visited the honeypot will block the bot ip address -->

<a href="/api/this-is-a-secret" class="hidden-link">ip blocker</a>
<!-- honeypot 2: endless uri generator -->
<!-- another hidden link points to a dynamic uri generator  -->
<!-- so if you visit the uri let's say dynamic/1 it will point you to dynamic/2 and so on -->
<!-- this technic makes web crawlers stuck at usless links -->
<a href="/secret-page/1" class="hidden-link">uri generator</a>

<style>
  .hidden-link {
    visibility: hidden;
  }
</style>
