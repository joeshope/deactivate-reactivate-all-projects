# deactivate-reactivate-all-projects

The purpose of this script is to run through Snyk Orgs to deactivate and reactivate all projects within. This will help rebuild the webhooks for SCM integration(s).

# Usage

1. Clone this repository locally

2. Define your Snyk API token (You can find your token in your [General Account Settings](https://app.snyk.io/account) after you login to Snyk.)
<pre><code>export SNYK_TOKEN={API_TOKEN}</code></pre>

3. Install required pip packages
<pre><code>pip install -r requirements.txt</code></pre>

4. Run the main.py script - define all required org(s) in the --orgs argument
<pre><code>python3 main.py --orgs "org-slug-1 org-slug-2"</code></pre>
