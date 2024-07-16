# deactivate-reactivate-all-projects

The purpose of this script is to run through Snyk Orgs to deactivate and reactivate all projects within. This will help rebuild the webhooks for SCM integration(s).

# Usage

1. Clone this repository locally

2. Define your Snyk API token
<pre><code>export SNYK_TOKEN={API_TOKEN}</code></pre>

3. Install required pip packages
<pre><code>pip install -r requirements.txt</code></pre>

4. Run the main.py script - define all required org(s) in the --orgs argument
example: <pre><code>python3 main.py --orgs "org-slug-1 org-slug-2"</code></pre>
