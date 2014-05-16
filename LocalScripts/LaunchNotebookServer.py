




<!DOCTYPE html>
<html class="   ">
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# object: http://ogp.me/ns/object# article: http://ogp.me/ns/article# profile: http://ogp.me/ns/profile#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    
    
    <title>UCSD_BigData/LocalScripts/LaunchNotebookServer.py at master · yoavfreund/UCSD_BigData</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub" />
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub" />
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-144.png" />
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144.png" />
    <meta property="fb:app_id" content="1401488693436528"/>

      <meta content="@github" name="twitter:site" /><meta content="summary" name="twitter:card" /><meta content="yoavfreund/UCSD_BigData" name="twitter:title" /><meta content="UCSD_BigData - A repository for scripts and notebooks for the UCSD big data course" name="twitter:description" /><meta content="https://avatars2.githubusercontent.com/u/1767644?s=400" name="twitter:image:src" />
<meta content="GitHub" property="og:site_name" /><meta content="object" property="og:type" /><meta content="https://avatars2.githubusercontent.com/u/1767644?s=400" property="og:image" /><meta content="yoavfreund/UCSD_BigData" property="og:title" /><meta content="https://github.com/yoavfreund/UCSD_BigData" property="og:url" /><meta content="UCSD_BigData - A repository for scripts and notebooks for the UCSD big data course" property="og:description" />

    <link rel="assets" href="https://assets-cdn.github.com/">
    <link rel="conduit-xhr" href="https://ghconduit.com:25035/">
    <link rel="xhr-socket" href="/_sockets" />

    <meta name="msapplication-TileImage" content="/windows-tile.png" />
    <meta name="msapplication-TileColor" content="#ffffff" />
    <meta name="selected-link" value="repo_source" data-pjax-transient />
    <meta content="collector.githubapp.com" name="octolytics-host" /><meta content="collector-cdn.github.com" name="octolytics-script-host" /><meta content="github" name="octolytics-app-id" /><meta content="80363097:303F:266E6D7:53756BE5" name="octolytics-dimension-request_id" /><meta content="4227812" name="octolytics-actor-id" /><meta content="woerns" name="octolytics-actor-login" /><meta content="02da811f55b982502217a52f448528e3b9e36e590839be54198a3c15f97b68c6" name="octolytics-actor-hash" />
    

    
    
    <link rel="icon" type="image/x-icon" href="https://assets-cdn.github.com/favicon.ico" />

    <meta content="authenticity_token" name="csrf-param" />
<meta content="aIT+3jxy967BR70wTvN8NIeYmUSOtksXbON6AdCWQezTktfAYCKX5J1cmuqZU7v9/YnMlPINLJkh77opQHtTjg==" name="csrf-token" />

    <link href="https://assets-cdn.github.com/assets/github-7a5c829a2dcdb70659835058a8c94aa55b3de51b.css" media="all" rel="stylesheet" type="text/css" />
    <link href="https://assets-cdn.github.com/assets/github2-50bd4d5d683bdda80f061b5d079826bd642a2787.css" media="all" rel="stylesheet" type="text/css" />
    


    <meta http-equiv="x-pjax-version" content="27ddb530b3558a176406a5a2294a1645">

      
  <meta name="description" content="UCSD_BigData - A repository for scripts and notebooks for the UCSD big data course" />

  <meta content="1767644" name="octolytics-dimension-user_id" /><meta content="yoavfreund" name="octolytics-dimension-user_login" /><meta content="17647752" name="octolytics-dimension-repository_id" /><meta content="yoavfreund/UCSD_BigData" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="false" name="octolytics-dimension-repository_is_fork" /><meta content="17647752" name="octolytics-dimension-repository_network_root_id" /><meta content="yoavfreund/UCSD_BigData" name="octolytics-dimension-repository_network_root_nwo" />
  <link href="https://github.com/yoavfreund/UCSD_BigData/commits/master.atom" rel="alternate" title="Recent Commits to UCSD_BigData:master" type="application/atom+xml" />

  </head>


  <body class="logged_in  env-production windows vis-public page-blob">
    <a href="#start-of-content" tabindex="1" class="accessibility-aid js-skip-to-content">Skip to content</a>
    <div class="wrapper">
      
      
      
      


      <div class="header header-logged-in true">
  <div class="container clearfix">

    <a class="header-logo-invertocat" href="https://github.com/">
  <span class="mega-octicon octicon-mark-github"></span>
</a>

    
    <a href="/notifications" aria-label="You have no unread notifications" class="notification-indicator tooltipped tooltipped-s" data-hotkey="g n">
        <span class="mail-status all-read"></span>
</a>

      <div class="command-bar js-command-bar  in-repository">
          <form accept-charset="UTF-8" action="/search" class="command-bar-form" id="top_search_form" method="get">

<div class="commandbar">
  <span class="message"></span>
  <input type="text" data-hotkey="s" name="q" id="js-command-bar-field" placeholder="Search or type a command" tabindex="1" autocapitalize="off"
    
    data-username="woerns"
      data-repo="yoavfreund/UCSD_BigData"
      data-branch="master"
      data-sha="73e5b323283ed664ba27b7d949b35a0ce0d8ff33"
  >
  <div class="display hidden"></div>
</div>

    <input type="hidden" name="nwo" value="yoavfreund/UCSD_BigData" />

    <div class="select-menu js-menu-container js-select-menu search-context-select-menu">
      <span class="minibutton select-menu-button js-menu-target" role="button" aria-haspopup="true">
        <span class="js-select-button">This repository</span>
      </span>

      <div class="select-menu-modal-holder js-menu-content js-navigation-container" aria-hidden="true">
        <div class="select-menu-modal">

          <div class="select-menu-item js-navigation-item js-this-repository-navigation-item selected">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" class="js-search-this-repository" name="search_target" value="repository" checked="checked" />
            <div class="select-menu-item-text js-select-button-text">This repository</div>
          </div> <!-- /.select-menu-item -->

          <div class="select-menu-item js-navigation-item js-all-repositories-navigation-item">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" name="search_target" value="global" />
            <div class="select-menu-item-text js-select-button-text">All repositories</div>
          </div> <!-- /.select-menu-item -->

        </div>
      </div>
    </div>

  <span class="help tooltipped tooltipped-s" aria-label="Show command bar help">
    <span class="octicon octicon-question"></span>
  </span>


  <input type="hidden" name="ref" value="cmdform">

</form>
        <ul class="top-nav">
          <li class="explore"><a href="/explore">Explore</a></li>
            <li><a href="https://gist.github.com">Gist</a></li>
            <li><a href="/blog">Blog</a></li>
          <li><a href="https://help.github.com">Help</a></li>
        </ul>
      </div>

    


  <ul id="user-links">
    <li>
      <a href="/woerns" class="name">
        <img alt="woerns" class=" js-avatar" data-user="4227812" height="20" src="https://avatars0.githubusercontent.com/u/4227812?s=140" width="20" /> woerns
      </a>
    </li>

    <li class="new-menu dropdown-toggle js-menu-container">
      <a href="#" class="js-menu-target tooltipped tooltipped-s" aria-label="Create new...">
        <span class="octicon octicon-plus"></span>
        <span class="dropdown-arrow"></span>
      </a>

      <div class="new-menu-content js-menu-content">
      </div>
    </li>

    <li>
      <a href="/settings/profile" id="account_settings"
        class="tooltipped tooltipped-s"
        aria-label="Account settings ">
        <span class="octicon octicon-tools"></span>
      </a>
    </li>
    <li>
      <form class="logout-form" action="/logout" method="post">
        <button class="sign-out-button tooltipped tooltipped-s" aria-label="Sign out">
          <span class="octicon octicon-log-out"></span>
        </button>
      </form>
    </li>

  </ul>

<div class="js-new-dropdown-contents hidden">
  

<ul class="dropdown-menu">
  <li>
    <a href="/new"><span class="octicon octicon-repo-create"></span> New repository</a>
  </li>
  <li>
    <a href="/organizations/new"><span class="octicon octicon-organization"></span> New organization</a>
  </li>


    <li class="section-title">
      <span title="yoavfreund/UCSD_BigData">This repository</span>
    </li>
      <li>
        <a href="/yoavfreund/UCSD_BigData/issues/new"><span class="octicon octicon-issue-opened"></span> New issue</a>
      </li>
</ul>

</div>


    
  </div>
</div>

      

        



      <div id="start-of-content" class="accessibility-aid"></div>
          <div class="site" itemscope itemtype="http://schema.org/WebPage">
    <div id="js-flash-container">
      
    </div>
    <div class="pagehead repohead instapaper_ignore readability-menu">
      <div class="container">
        

<ul class="pagehead-actions">

    <li class="subscription">
      <form accept-charset="UTF-8" action="/notifications/subscribe" class="js-social-container" data-autosubmit="true" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="authenticity_token" type="hidden" value="nxHjiB1MZEp9+ZGybBOcnAMJWxgyWbtoxi08pkK3R46D6w6aQ09OAYpPGKZb1B8VFByCourHBxRwbf481Z0lwA==" /></div>  <input id="repository_id" name="repository_id" type="hidden" value="17647752" />

    <div class="select-menu js-menu-container js-select-menu">
      <a class="social-count js-social-count" href="/yoavfreund/UCSD_BigData/watchers">
        4
      </a>
      <span class="minibutton select-menu-button with-count js-menu-target" role="button" tabindex="0" aria-haspopup="true">
        <span class="js-select-button">
          <span class="octicon octicon-eye-watch"></span>
          Watch
        </span>
      </span>

      <div class="select-menu-modal-holder">
        <div class="select-menu-modal subscription-menu-modal js-menu-content" aria-hidden="true">
          <div class="select-menu-header">
            <span class="select-menu-title">Notification status</span>
            <span class="octicon octicon-remove-close js-menu-close"></span>
          </div> <!-- /.select-menu-header -->

          <div class="select-menu-list js-navigation-container" role="menu">

            <div class="select-menu-item js-navigation-item selected" role="menuitem" tabindex="0">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <div class="select-menu-item-text">
                <input checked="checked" id="do_included" name="do" type="radio" value="included" />
                <h4>Not watching</h4>
                <span class="description">You only receive notifications for conversations in which you participate or are @mentioned.</span>
                <span class="js-select-button-text hidden-select-button-text">
                  <span class="octicon octicon-eye-watch"></span>
                  Watch
                </span>
              </div>
            </div> <!-- /.select-menu-item -->

            <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
              <span class="select-menu-item-icon octicon octicon octicon-check"></span>
              <div class="select-menu-item-text">
                <input id="do_subscribed" name="do" type="radio" value="subscribed" />
                <h4>Watching</h4>
                <span class="description">You receive notifications for all conversations in this repository.</span>
                <span class="js-select-button-text hidden-select-button-text">
                  <span class="octicon octicon-eye-unwatch"></span>
                  Unwatch
                </span>
              </div>
            </div> <!-- /.select-menu-item -->

            <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <div class="select-menu-item-text">
                <input id="do_ignore" name="do" type="radio" value="ignore" />
                <h4>Ignoring</h4>
                <span class="description">You do not receive any notifications for conversations in this repository.</span>
                <span class="js-select-button-text hidden-select-button-text">
                  <span class="octicon octicon-mute"></span>
                  Stop ignoring
                </span>
              </div>
            </div> <!-- /.select-menu-item -->

          </div> <!-- /.select-menu-list -->

        </div> <!-- /.select-menu-modal -->
      </div> <!-- /.select-menu-modal-holder -->
    </div> <!-- /.select-menu -->

</form>
    </li>

  <li>
  

  <div class="js-toggler-container js-social-container starring-container ">

    <form accept-charset="UTF-8" action="/yoavfreund/UCSD_BigData/unstar" class="js-toggler-form starred" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="authenticity_token" type="hidden" value="LD/dvwTwKxaud1ON6U0ccBxs40HnP2uC1eS5fG+LFkc9a7CJp3ErCjlJ8QzdZQyeZ9E/0eqL5TrW7yRZ+vcuaA==" /></div>
      <button
        class="minibutton with-count js-toggler-target star-button"
        aria-label="Unstar this repository" title="Unstar yoavfreund/UCSD_BigData">
        <span class="octicon octicon-star-delete"></span><span class="text">Unstar</span>
      </button>
        <a class="social-count js-social-count" href="/yoavfreund/UCSD_BigData/stargazers">
          0
        </a>
</form>
    <form accept-charset="UTF-8" action="/yoavfreund/UCSD_BigData/star" class="js-toggler-form unstarred" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="authenticity_token" type="hidden" value="FnTfVnhO3EqhcNEu3VGXbmajL2IaPFR/Hko9Zp5H6eWUN3yj9VM3gzz/5EG1ncHUIuKARFn9pXj1L8X8IYzaXg==" /></div>
      <button
        class="minibutton with-count js-toggler-target star-button"
        aria-label="Star this repository" title="Star yoavfreund/UCSD_BigData">
        <span class="octicon octicon-star"></span><span class="text">Star</span>
      </button>
        <a class="social-count js-social-count" href="/yoavfreund/UCSD_BigData/stargazers">
          0
        </a>
</form>  </div>

  </li>


        <li>
          <a href="/yoavfreund/UCSD_BigData/fork" class="minibutton with-count js-toggler-target fork-button lighter tooltipped-n" title="Fork your own copy of yoavfreund/UCSD_BigData to your account" aria-label="Fork your own copy of yoavfreund/UCSD_BigData to your account" rel="facebox nofollow">
            <span class="octicon octicon-git-branch-create"></span><span class="text">Fork</span>
          </a>
          <a href="/yoavfreund/UCSD_BigData/network" class="social-count">44</a>
        </li>


</ul>

        <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public">
          <span class="repo-label"><span>public</span></span>
          <span class="mega-octicon octicon-repo"></span>
          <span class="author"><a href="/yoavfreund" class="url fn" itemprop="url" rel="author"><span itemprop="title">yoavfreund</span></a></span><!--
       --><span class="path-divider">/</span><!--
       --><strong><a href="/yoavfreund/UCSD_BigData" class="js-current-repository js-repo-home-link">UCSD_BigData</a></strong>

          <span class="page-context-loader">
            <img alt="Octocat-spinner-32" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
          </span>

        </h1>
      </div><!-- /.container -->
    </div><!-- /.repohead -->

    <div class="container">
      <div class="repository-with-sidebar repo-container new-discussion-timeline js-new-discussion-timeline  ">
        <div class="repository-sidebar clearfix">
            

<div class="sunken-menu vertical-right repo-nav js-repo-nav js-repository-container-pjax js-octicon-loaders">
  <div class="sunken-menu-contents">
    <ul class="sunken-menu-group">
      <li class="tooltipped tooltipped-w" aria-label="Code">
        <a href="/yoavfreund/UCSD_BigData" aria-label="Code" class="selected js-selected-navigation-item sunken-menu-item" data-hotkey="g c" data-pjax="true" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches /yoavfreund/UCSD_BigData">
          <span class="octicon octicon-code"></span> <span class="full-word">Code</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

        <li class="tooltipped tooltipped-w" aria-label="Issues">
          <a href="/yoavfreund/UCSD_BigData/issues" aria-label="Issues" class="js-selected-navigation-item sunken-menu-item js-disable-pjax" data-hotkey="g i" data-selected-links="repo_issues /yoavfreund/UCSD_BigData/issues">
            <span class="octicon octicon-issue-opened"></span> <span class="full-word">Issues</span>
            <span class='counter'>0</span>
            <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>        </li>

      <li class="tooltipped tooltipped-w" aria-label="Pull Requests">
        <a href="/yoavfreund/UCSD_BigData/pulls" aria-label="Pull Requests" class="js-selected-navigation-item sunken-menu-item js-disable-pjax" data-hotkey="g p" data-selected-links="repo_pulls /yoavfreund/UCSD_BigData/pulls">
            <span class="octicon octicon-git-pull-request"></span> <span class="full-word">Pull Requests</span>
            <span class='counter'>0</span>
            <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>


        <li class="tooltipped tooltipped-w" aria-label="Wiki">
          <a href="/yoavfreund/UCSD_BigData/wiki" aria-label="Wiki" class="js-selected-navigation-item sunken-menu-item js-disable-pjax" data-hotkey="g w" data-selected-links="repo_wiki /yoavfreund/UCSD_BigData/wiki">
            <span class="octicon octicon-book"></span> <span class="full-word">Wiki</span>
            <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>        </li>
    </ul>
    <div class="sunken-menu-separator"></div>
    <ul class="sunken-menu-group">

      <li class="tooltipped tooltipped-w" aria-label="Pulse">
        <a href="/yoavfreund/UCSD_BigData/pulse" aria-label="Pulse" class="js-selected-navigation-item sunken-menu-item" data-pjax="true" data-selected-links="pulse /yoavfreund/UCSD_BigData/pulse">
          <span class="octicon octicon-pulse"></span> <span class="full-word">Pulse</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

      <li class="tooltipped tooltipped-w" aria-label="Graphs">
        <a href="/yoavfreund/UCSD_BigData/graphs" aria-label="Graphs" class="js-selected-navigation-item sunken-menu-item" data-pjax="true" data-selected-links="repo_graphs repo_contributors /yoavfreund/UCSD_BigData/graphs">
          <span class="octicon octicon-graph"></span> <span class="full-word">Graphs</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

      <li class="tooltipped tooltipped-w" aria-label="Network">
        <a href="/yoavfreund/UCSD_BigData/network" aria-label="Network" class="js-selected-navigation-item sunken-menu-item js-disable-pjax" data-selected-links="repo_network /yoavfreund/UCSD_BigData/network">
          <span class="octicon octicon-git-branch"></span> <span class="full-word">Network</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>
    </ul>


  </div>
</div>

              <div class="only-with-full-nav">
                

  

<div class="clone-url "
  data-protocol-type="http"
  data-url="/users/set_protocol?protocol_selector=http&amp;protocol_type=clone">
  <h3><strong>HTTPS</strong> clone URL</h3>
  <div class="clone-url-box">
    <input type="text" class="clone js-url-field"
           value="https://github.com/yoavfreund/UCSD_BigData.git" readonly="readonly">
    <span class="url-box-clippy">
    <button aria-label="copy to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-clipboard-text="https://github.com/yoavfreund/UCSD_BigData.git" data-copied-hint="copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>

  

<div class="clone-url open"
  data-protocol-type="ssh"
  data-url="/users/set_protocol?protocol_selector=ssh&amp;protocol_type=clone">
  <h3><strong>SSH</strong> clone URL</h3>
  <div class="clone-url-box">
    <input type="text" class="clone js-url-field"
           value="git@github.com:yoavfreund/UCSD_BigData.git" readonly="readonly">
    <span class="url-box-clippy">
    <button aria-label="copy to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-clipboard-text="git@github.com:yoavfreund/UCSD_BigData.git" data-copied-hint="copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>

  

<div class="clone-url "
  data-protocol-type="subversion"
  data-url="/users/set_protocol?protocol_selector=subversion&amp;protocol_type=clone">
  <h3><strong>Subversion</strong> checkout URL</h3>
  <div class="clone-url-box">
    <input type="text" class="clone js-url-field"
           value="https://github.com/yoavfreund/UCSD_BigData" readonly="readonly">
    <span class="url-box-clippy">
    <button aria-label="copy to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-clipboard-text="https://github.com/yoavfreund/UCSD_BigData" data-copied-hint="copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>


<p class="clone-options">You can clone with
      <a href="#" class="js-clone-selector" data-protocol="http">HTTPS</a>,
      <a href="#" class="js-clone-selector" data-protocol="ssh">SSH</a>,
      or <a href="#" class="js-clone-selector" data-protocol="subversion">Subversion</a>.
  <span class="help tooltipped tooltipped-n" aria-label="Get help on which URL is right for you.">
    <a href="https://help.github.com/articles/which-remote-url-should-i-use">
    <span class="octicon octicon-question"></span>
    </a>
  </span>
</p>


  <a href="github-windows://openRepo/https://github.com/yoavfreund/UCSD_BigData" class="minibutton sidebar-button" title="Save yoavfreund/UCSD_BigData to your computer and use it in GitHub Desktop." aria-label="Save yoavfreund/UCSD_BigData to your computer and use it in GitHub Desktop.">
    <span class="octicon octicon-device-desktop"></span>
    Clone in Desktop
  </a>

                <a href="/yoavfreund/UCSD_BigData/archive/master.zip"
                   class="minibutton sidebar-button"
                   aria-label="Download yoavfreund/UCSD_BigData as a zip file"
                   title="Download yoavfreund/UCSD_BigData as a zip file"
                   rel="nofollow">
                  <span class="octicon octicon-cloud-download"></span>
                  Download ZIP
                </a>
              </div>
        </div><!-- /.repository-sidebar -->

        <div id="js-repo-pjax-container" class="repository-content context-loader-container" data-pjax-container>
          


<a href="/yoavfreund/UCSD_BigData/blob/5e66d4734598b2255c9f78d1952fc025672bd9e3/LocalScripts/LaunchNotebookServer.py" class="hidden js-permalink-shortcut" data-hotkey="y">Permalink</a>

<!-- blob contrib key: blob_contributors:v21:17fe3a50d39db4870c28631abe0197f0 -->

<p title="This is a placeholder element" class="js-history-link-replace hidden"></p>

<a href="/yoavfreund/UCSD_BigData/find/master" data-pjax data-hotkey="t" class="js-show-file-finder" style="display:none">Show File Finder</a>

<div class="file-navigation">
  

<div class="select-menu js-menu-container js-select-menu" >
  <span class="minibutton select-menu-button js-menu-target" data-hotkey="w"
    data-master-branch="master"
    data-ref="master"
    role="button" aria-label="Switch branches or tags" tabindex="0" aria-haspopup="true">
    <span class="octicon octicon-git-branch"></span>
    <i>branch:</i>
    <span class="js-select-button">master</span>
  </span>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax aria-hidden="true">

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <span class="select-menu-title">Switch branches/tags</span>
        <span class="octicon octicon-remove-close js-menu-close"></span>
      </div> <!-- /.select-menu-header -->

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Filter branches/tags" id="context-commitish-filter-field" class="js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" class="js-select-menu-tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" class="js-select-menu-tab">Tags</a>
            </li>
          </ul>
        </div><!-- /.select-menu-tabs -->
      </div><!-- /.select-menu-filters -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/yoavfreund/UCSD_BigData/blob/gh-pages/LocalScripts/LaunchNotebookServer.py"
                 data-name="gh-pages"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="gh-pages">gh-pages</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item selected">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/yoavfreund/UCSD_BigData/blob/master/LocalScripts/LaunchNotebookServer.py"
                 data-name="master"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="master">master</a>
            </div> <!-- /.select-menu-item -->
        </div>

          <div class="select-menu-no-results">Nothing to show</div>
      </div> <!-- /.select-menu-list -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div> <!-- /.select-menu-list -->

    </div> <!-- /.select-menu-modal -->
  </div> <!-- /.select-menu-modal-holder -->
</div> <!-- /.select-menu -->

  <div class="breadcrumb">
    <span class='repo-root js-repo-root'><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/yoavfreund/UCSD_BigData" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">UCSD_BigData</span></a></span></span><span class="separator"> / </span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/yoavfreund/UCSD_BigData/tree/master/LocalScripts" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">LocalScripts</span></a></span><span class="separator"> / </span><strong class="final-path">LaunchNotebookServer.py</strong> <button aria-label="copy to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-clipboard-text="LocalScripts/LaunchNotebookServer.py" data-copied-hint="copied!" type="button"><span class="octicon octicon-clippy"></span></button>
  </div>
</div>


  <div class="commit commit-loader file-history-tease js-deferred-content" data-url="/yoavfreund/UCSD_BigData/contributors/master/LocalScripts/LaunchNotebookServer.py">
    Fetching contributors…

    <div class="participation">
      <p class="loader-loading"><img alt="Octocat-spinner-32-eaf2f5" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32-EAF2F5.gif" width="16" /></p>
      <p class="loader-error">Cannot retrieve contributors at this time</p>
    </div>
  </div>

<div class="file-box">
  <div class="file">
    <div class="meta clearfix">
      <div class="info file-name">
        <span class="icon"><b class="octicon octicon-file-text"></b></span>
        <span class="mode" title="File Mode">executable file</span>
        <span class="meta-divider"></span>
          <span>284 lines (228 sloc)</span>
          <span class="meta-divider"></span>
        <span>11.906 kb</span>
      </div>
      <div class="actions">
        <div class="button-group">
            <a class="minibutton tooltipped tooltipped-w"
               href="github-windows://openRepo/https://github.com/yoavfreund/UCSD_BigData?branch=master&amp;filepath=LocalScripts%2FLaunchNotebookServer.py" aria-label="Open this file in GitHub for Windows">
                <span class="octicon octicon-device-desktop"></span> Open
            </a>
                <a class="minibutton tooltipped tooltipped-n js-update-url-with-hash"
                   aria-label="Clicking this button will automatically fork this project so you can edit the file"
                   href="/yoavfreund/UCSD_BigData/edit/master/LocalScripts/LaunchNotebookServer.py"
                   data-method="post" rel="nofollow">Edit</a>
          <a href="/yoavfreund/UCSD_BigData/raw/master/LocalScripts/LaunchNotebookServer.py" class="button minibutton " id="raw-url">Raw</a>
            <a href="/yoavfreund/UCSD_BigData/blame/master/LocalScripts/LaunchNotebookServer.py" class="button minibutton js-update-url-with-hash">Blame</a>
          <a href="/yoavfreund/UCSD_BigData/commits/master/LocalScripts/LaunchNotebookServer.py" class="button minibutton " rel="nofollow">History</a>
        </div><!-- /.button-group -->

            <a class="minibutton danger empty-icon tooltipped tooltipped-s"
               href="/yoavfreund/UCSD_BigData/delete/master/LocalScripts/LaunchNotebookServer.py"
               aria-label="Fork this project and delete file"
               data-method="post" data-test-id="delete-blob-file" rel="nofollow">

          Delete
        </a>
      </div><!-- /.actions -->
    </div>
        <div class="blob-wrapper data type-python js-blob-data">
        <table class="file-code file-diff tab-size-8">
          <tr class="file-code-line">
            <td class="blob-line-nums">
              <span id="L1" rel="#L1">1</span>
<span id="L2" rel="#L2">2</span>
<span id="L3" rel="#L3">3</span>
<span id="L4" rel="#L4">4</span>
<span id="L5" rel="#L5">5</span>
<span id="L6" rel="#L6">6</span>
<span id="L7" rel="#L7">7</span>
<span id="L8" rel="#L8">8</span>
<span id="L9" rel="#L9">9</span>
<span id="L10" rel="#L10">10</span>
<span id="L11" rel="#L11">11</span>
<span id="L12" rel="#L12">12</span>
<span id="L13" rel="#L13">13</span>
<span id="L14" rel="#L14">14</span>
<span id="L15" rel="#L15">15</span>
<span id="L16" rel="#L16">16</span>
<span id="L17" rel="#L17">17</span>
<span id="L18" rel="#L18">18</span>
<span id="L19" rel="#L19">19</span>
<span id="L20" rel="#L20">20</span>
<span id="L21" rel="#L21">21</span>
<span id="L22" rel="#L22">22</span>
<span id="L23" rel="#L23">23</span>
<span id="L24" rel="#L24">24</span>
<span id="L25" rel="#L25">25</span>
<span id="L26" rel="#L26">26</span>
<span id="L27" rel="#L27">27</span>
<span id="L28" rel="#L28">28</span>
<span id="L29" rel="#L29">29</span>
<span id="L30" rel="#L30">30</span>
<span id="L31" rel="#L31">31</span>
<span id="L32" rel="#L32">32</span>
<span id="L33" rel="#L33">33</span>
<span id="L34" rel="#L34">34</span>
<span id="L35" rel="#L35">35</span>
<span id="L36" rel="#L36">36</span>
<span id="L37" rel="#L37">37</span>
<span id="L38" rel="#L38">38</span>
<span id="L39" rel="#L39">39</span>
<span id="L40" rel="#L40">40</span>
<span id="L41" rel="#L41">41</span>
<span id="L42" rel="#L42">42</span>
<span id="L43" rel="#L43">43</span>
<span id="L44" rel="#L44">44</span>
<span id="L45" rel="#L45">45</span>
<span id="L46" rel="#L46">46</span>
<span id="L47" rel="#L47">47</span>
<span id="L48" rel="#L48">48</span>
<span id="L49" rel="#L49">49</span>
<span id="L50" rel="#L50">50</span>
<span id="L51" rel="#L51">51</span>
<span id="L52" rel="#L52">52</span>
<span id="L53" rel="#L53">53</span>
<span id="L54" rel="#L54">54</span>
<span id="L55" rel="#L55">55</span>
<span id="L56" rel="#L56">56</span>
<span id="L57" rel="#L57">57</span>
<span id="L58" rel="#L58">58</span>
<span id="L59" rel="#L59">59</span>
<span id="L60" rel="#L60">60</span>
<span id="L61" rel="#L61">61</span>
<span id="L62" rel="#L62">62</span>
<span id="L63" rel="#L63">63</span>
<span id="L64" rel="#L64">64</span>
<span id="L65" rel="#L65">65</span>
<span id="L66" rel="#L66">66</span>
<span id="L67" rel="#L67">67</span>
<span id="L68" rel="#L68">68</span>
<span id="L69" rel="#L69">69</span>
<span id="L70" rel="#L70">70</span>
<span id="L71" rel="#L71">71</span>
<span id="L72" rel="#L72">72</span>
<span id="L73" rel="#L73">73</span>
<span id="L74" rel="#L74">74</span>
<span id="L75" rel="#L75">75</span>
<span id="L76" rel="#L76">76</span>
<span id="L77" rel="#L77">77</span>
<span id="L78" rel="#L78">78</span>
<span id="L79" rel="#L79">79</span>
<span id="L80" rel="#L80">80</span>
<span id="L81" rel="#L81">81</span>
<span id="L82" rel="#L82">82</span>
<span id="L83" rel="#L83">83</span>
<span id="L84" rel="#L84">84</span>
<span id="L85" rel="#L85">85</span>
<span id="L86" rel="#L86">86</span>
<span id="L87" rel="#L87">87</span>
<span id="L88" rel="#L88">88</span>
<span id="L89" rel="#L89">89</span>
<span id="L90" rel="#L90">90</span>
<span id="L91" rel="#L91">91</span>
<span id="L92" rel="#L92">92</span>
<span id="L93" rel="#L93">93</span>
<span id="L94" rel="#L94">94</span>
<span id="L95" rel="#L95">95</span>
<span id="L96" rel="#L96">96</span>
<span id="L97" rel="#L97">97</span>
<span id="L98" rel="#L98">98</span>
<span id="L99" rel="#L99">99</span>
<span id="L100" rel="#L100">100</span>
<span id="L101" rel="#L101">101</span>
<span id="L102" rel="#L102">102</span>
<span id="L103" rel="#L103">103</span>
<span id="L104" rel="#L104">104</span>
<span id="L105" rel="#L105">105</span>
<span id="L106" rel="#L106">106</span>
<span id="L107" rel="#L107">107</span>
<span id="L108" rel="#L108">108</span>
<span id="L109" rel="#L109">109</span>
<span id="L110" rel="#L110">110</span>
<span id="L111" rel="#L111">111</span>
<span id="L112" rel="#L112">112</span>
<span id="L113" rel="#L113">113</span>
<span id="L114" rel="#L114">114</span>
<span id="L115" rel="#L115">115</span>
<span id="L116" rel="#L116">116</span>
<span id="L117" rel="#L117">117</span>
<span id="L118" rel="#L118">118</span>
<span id="L119" rel="#L119">119</span>
<span id="L120" rel="#L120">120</span>
<span id="L121" rel="#L121">121</span>
<span id="L122" rel="#L122">122</span>
<span id="L123" rel="#L123">123</span>
<span id="L124" rel="#L124">124</span>
<span id="L125" rel="#L125">125</span>
<span id="L126" rel="#L126">126</span>
<span id="L127" rel="#L127">127</span>
<span id="L128" rel="#L128">128</span>
<span id="L129" rel="#L129">129</span>
<span id="L130" rel="#L130">130</span>
<span id="L131" rel="#L131">131</span>
<span id="L132" rel="#L132">132</span>
<span id="L133" rel="#L133">133</span>
<span id="L134" rel="#L134">134</span>
<span id="L135" rel="#L135">135</span>
<span id="L136" rel="#L136">136</span>
<span id="L137" rel="#L137">137</span>
<span id="L138" rel="#L138">138</span>
<span id="L139" rel="#L139">139</span>
<span id="L140" rel="#L140">140</span>
<span id="L141" rel="#L141">141</span>
<span id="L142" rel="#L142">142</span>
<span id="L143" rel="#L143">143</span>
<span id="L144" rel="#L144">144</span>
<span id="L145" rel="#L145">145</span>
<span id="L146" rel="#L146">146</span>
<span id="L147" rel="#L147">147</span>
<span id="L148" rel="#L148">148</span>
<span id="L149" rel="#L149">149</span>
<span id="L150" rel="#L150">150</span>
<span id="L151" rel="#L151">151</span>
<span id="L152" rel="#L152">152</span>
<span id="L153" rel="#L153">153</span>
<span id="L154" rel="#L154">154</span>
<span id="L155" rel="#L155">155</span>
<span id="L156" rel="#L156">156</span>
<span id="L157" rel="#L157">157</span>
<span id="L158" rel="#L158">158</span>
<span id="L159" rel="#L159">159</span>
<span id="L160" rel="#L160">160</span>
<span id="L161" rel="#L161">161</span>
<span id="L162" rel="#L162">162</span>
<span id="L163" rel="#L163">163</span>
<span id="L164" rel="#L164">164</span>
<span id="L165" rel="#L165">165</span>
<span id="L166" rel="#L166">166</span>
<span id="L167" rel="#L167">167</span>
<span id="L168" rel="#L168">168</span>
<span id="L169" rel="#L169">169</span>
<span id="L170" rel="#L170">170</span>
<span id="L171" rel="#L171">171</span>
<span id="L172" rel="#L172">172</span>
<span id="L173" rel="#L173">173</span>
<span id="L174" rel="#L174">174</span>
<span id="L175" rel="#L175">175</span>
<span id="L176" rel="#L176">176</span>
<span id="L177" rel="#L177">177</span>
<span id="L178" rel="#L178">178</span>
<span id="L179" rel="#L179">179</span>
<span id="L180" rel="#L180">180</span>
<span id="L181" rel="#L181">181</span>
<span id="L182" rel="#L182">182</span>
<span id="L183" rel="#L183">183</span>
<span id="L184" rel="#L184">184</span>
<span id="L185" rel="#L185">185</span>
<span id="L186" rel="#L186">186</span>
<span id="L187" rel="#L187">187</span>
<span id="L188" rel="#L188">188</span>
<span id="L189" rel="#L189">189</span>
<span id="L190" rel="#L190">190</span>
<span id="L191" rel="#L191">191</span>
<span id="L192" rel="#L192">192</span>
<span id="L193" rel="#L193">193</span>
<span id="L194" rel="#L194">194</span>
<span id="L195" rel="#L195">195</span>
<span id="L196" rel="#L196">196</span>
<span id="L197" rel="#L197">197</span>
<span id="L198" rel="#L198">198</span>
<span id="L199" rel="#L199">199</span>
<span id="L200" rel="#L200">200</span>
<span id="L201" rel="#L201">201</span>
<span id="L202" rel="#L202">202</span>
<span id="L203" rel="#L203">203</span>
<span id="L204" rel="#L204">204</span>
<span id="L205" rel="#L205">205</span>
<span id="L206" rel="#L206">206</span>
<span id="L207" rel="#L207">207</span>
<span id="L208" rel="#L208">208</span>
<span id="L209" rel="#L209">209</span>
<span id="L210" rel="#L210">210</span>
<span id="L211" rel="#L211">211</span>
<span id="L212" rel="#L212">212</span>
<span id="L213" rel="#L213">213</span>
<span id="L214" rel="#L214">214</span>
<span id="L215" rel="#L215">215</span>
<span id="L216" rel="#L216">216</span>
<span id="L217" rel="#L217">217</span>
<span id="L218" rel="#L218">218</span>
<span id="L219" rel="#L219">219</span>
<span id="L220" rel="#L220">220</span>
<span id="L221" rel="#L221">221</span>
<span id="L222" rel="#L222">222</span>
<span id="L223" rel="#L223">223</span>
<span id="L224" rel="#L224">224</span>
<span id="L225" rel="#L225">225</span>
<span id="L226" rel="#L226">226</span>
<span id="L227" rel="#L227">227</span>
<span id="L228" rel="#L228">228</span>
<span id="L229" rel="#L229">229</span>
<span id="L230" rel="#L230">230</span>
<span id="L231" rel="#L231">231</span>
<span id="L232" rel="#L232">232</span>
<span id="L233" rel="#L233">233</span>
<span id="L234" rel="#L234">234</span>
<span id="L235" rel="#L235">235</span>
<span id="L236" rel="#L236">236</span>
<span id="L237" rel="#L237">237</span>
<span id="L238" rel="#L238">238</span>
<span id="L239" rel="#L239">239</span>
<span id="L240" rel="#L240">240</span>
<span id="L241" rel="#L241">241</span>
<span id="L242" rel="#L242">242</span>
<span id="L243" rel="#L243">243</span>
<span id="L244" rel="#L244">244</span>
<span id="L245" rel="#L245">245</span>
<span id="L246" rel="#L246">246</span>
<span id="L247" rel="#L247">247</span>
<span id="L248" rel="#L248">248</span>
<span id="L249" rel="#L249">249</span>
<span id="L250" rel="#L250">250</span>
<span id="L251" rel="#L251">251</span>
<span id="L252" rel="#L252">252</span>
<span id="L253" rel="#L253">253</span>
<span id="L254" rel="#L254">254</span>
<span id="L255" rel="#L255">255</span>
<span id="L256" rel="#L256">256</span>
<span id="L257" rel="#L257">257</span>
<span id="L258" rel="#L258">258</span>
<span id="L259" rel="#L259">259</span>
<span id="L260" rel="#L260">260</span>
<span id="L261" rel="#L261">261</span>
<span id="L262" rel="#L262">262</span>
<span id="L263" rel="#L263">263</span>
<span id="L264" rel="#L264">264</span>
<span id="L265" rel="#L265">265</span>
<span id="L266" rel="#L266">266</span>
<span id="L267" rel="#L267">267</span>
<span id="L268" rel="#L268">268</span>
<span id="L269" rel="#L269">269</span>
<span id="L270" rel="#L270">270</span>
<span id="L271" rel="#L271">271</span>
<span id="L272" rel="#L272">272</span>
<span id="L273" rel="#L273">273</span>
<span id="L274" rel="#L274">274</span>
<span id="L275" rel="#L275">275</span>
<span id="L276" rel="#L276">276</span>
<span id="L277" rel="#L277">277</span>
<span id="L278" rel="#L278">278</span>
<span id="L279" rel="#L279">279</span>
<span id="L280" rel="#L280">280</span>
<span id="L281" rel="#L281">281</span>
<span id="L282" rel="#L282">282</span>
<span id="L283" rel="#L283">283</span>

            </td>
            <td class="blob-line-code"><div class="code-body highlight"><pre><div class='line' id='LC1'><span class="c">#!/usr/bin/env python</span></div><div class='line' id='LC2'><span class="sd">&quot;&quot;&quot;### A Script for Launching and managing an iPython notebook server on AWS ###</span></div><div class='line' id='LC3'><span class="sd"> # Written by Yoav Freund, March 2014</span></div><div class='line' id='LC4'><br/></div><div class='line' id='LC5'><span class="sd">### Before you run this script ###</span></div><div class='line' id='LC6'><span class="sd"> Before running this script, you need to install boto on your local machine (not ec2).</span></div><div class='line' id='LC7'><span class="sd"> See https://pypi.python.org/pypi/boto. </span></div><div class='line' id='LC8'><span class="sd"> You can use either &quot;sudo pip install boto&quot; or &quot;sudo easy_install boto&quot;</span></div><div class='line' id='LC9'><br/></div><div class='line' id='LC10'><span class="sd">### Security credentials ###</span></div><div class='line' id='LC11'><span class="sd"> In order to launch a notebook you need to first establish credentials on AWS. Set these credentials by editing the values in the file ../../Vault/AWSCredentials.py</span></div><div class='line' id='LC12'><br/></div><div class='line' id='LC13'><span class="sd">Here are the steps you need to follow to achieve this</span></div><div class='line' id='LC14'><br/></div><div class='line' id='LC15'><span class="sd"> 1. Open an AWS account  </span></div><div class='line' id='LC16'><span class="sd"> 2. Create a key-pair so that  you can connect securely to your instances.  </span></div><div class='line' id='LC17'><span class="sd"> 3. Create a Security group to define which IPs can connect to your instances and through which ports.</span></div><div class='line' id='LC18'><span class="sd"> You need to complete these steps only one time. Later sessions can use the same credentials. If you are registered to the</span></div><div class='line' id='LC19'><span class="sd"> class you will get a credit of $100 towards your use of AWS. To get this credit goto the page &quot;consolidated billing&quot; (xxxx) and send a request to the class instructor.</span></div><div class='line' id='LC20'><span class="sd"> </span></div><div class='line' id='LC21'><span class="sd"> #### Security credentials ####</span></div><div class='line' id='LC22'><span class="sd"> In order to start your EC2 Session you need two things:</span></div><div class='line' id='LC23'><span class="sd"> </span></div><div class='line' id='LC24'><span class="sd"> 1. A key-pair</span></div><div class='line' id='LC25'><span class="sd"> 2. A security group</span></div><div class='line' id='LC26'><span class="sd"> </span></div><div class='line' id='LC27'><span class="sd"> Before you try to connect to an EC2 instance make sure that the</span></div><div class='line' id='LC28'><span class="sd"> security group that you are using contains the IP address that you</span></div><div class='line' id='LC29'><span class="sd"> are connecting from. The security group estricts which IP addresses</span></div><div class='line' id='LC30'><span class="sd"> are allowed to connect to which ports. Best set using the AWS web</span></div><div class='line' id='LC31'><span class="sd"> interface.</span></div><div class='line' id='LC32'><br/></div><div class='line' id='LC33'><span class="sd"> Google &quot;my ip&quot; will give you your current address. Then go to the EC2</span></div><div class='line' id='LC34'><span class="sd"> web interface and make sure that you have rules for connecting from</span></div><div class='line' id='LC35'><span class="sd"> your current address to all of the ports.</span></div><div class='line' id='LC36'><br/></div><div class='line' id='LC37'><span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC38'><br/></div><div class='line' id='LC39'><span class="c"># ### Definitions of procedures ###</span></div><div class='line' id='LC40'><span class="kn">import</span> <span class="nn">boto.ec2</span></div><div class='line' id='LC41'><span class="kn">import</span> <span class="nn">time</span><span class="o">,</span> <span class="nn">pickle</span></div><div class='line' id='LC42'><span class="kn">import</span> <span class="nn">subprocess</span></div><div class='line' id='LC43'><span class="kn">import</span> <span class="nn">sys</span><span class="o">,</span><span class="nn">os</span><span class="o">,</span><span class="nn">re</span><span class="o">,</span><span class="nn">webbrowser</span><span class="o">,</span><span class="nn">select</span></div><div class='line' id='LC44'><span class="kn">from</span> <span class="nn">string</span> <span class="kn">import</span> <span class="n">rstrip</span></div><div class='line' id='LC45'><span class="kn">import</span> <span class="nn">argparse</span></div><div class='line' id='LC46'><br/></div><div class='line' id='LC47'><br/></div><div class='line' id='LC48'><span class="n">ami</span><span class="o">=</span><span class="s">&#39;ami-18d33e70&#39;</span>             <span class="c"># Image configured for big data class</span></div><div class='line' id='LC49'><span class="c"># AMI name: ERM_Utils These two lines last updated 5/11/2014</span></div><div class='line' id='LC50'><br/></div><div class='line' id='LC51'><span class="c"># Read Credentials </span></div><div class='line' id='LC52'><span class="k">try</span><span class="p">:</span></div><div class='line' id='LC53'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">vault</span><span class="o">=</span><span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="p">[</span><span class="s">&#39;EC2_VAULT&#39;</span><span class="p">]</span></div><div class='line' id='LC54'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">file</span><span class="o">=</span><span class="nb">open</span><span class="p">(</span><span class="n">vault</span><span class="o">+</span><span class="s">&#39;/Creds.pkl&#39;</span><span class="p">)</span></div><div class='line' id='LC55'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">ALL_Creds</span><span class="o">=</span><span class="n">pickle</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="nb">file</span><span class="p">)</span></div><div class='line' id='LC56'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">Creds</span><span class="o">=</span><span class="n">ALL_Creds</span><span class="p">[</span><span class="s">&#39;launcher&#39;</span><span class="p">]</span></div><div class='line' id='LC57'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="n">Creds</span></div><div class='line' id='LC58'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">aws_access_key_id</span><span class="o">=</span><span class="n">Creds</span><span class="p">[</span><span class="s">&#39;key_id&#39;</span><span class="p">]</span></div><div class='line' id='LC59'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">aws_secret_access_key</span><span class="o">=</span><span class="n">Creds</span><span class="p">[</span><span class="s">&#39;secret_key&#39;</span><span class="p">]</span></div><div class='line' id='LC60'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">user_name</span><span class="o">=</span><span class="n">Creds</span><span class="p">[</span><span class="s">&#39;ID&#39;</span><span class="p">]</span></div><div class='line' id='LC61'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">keyPairFile</span><span class="o">=</span><span class="n">Creds</span><span class="p">[</span><span class="s">&#39;ssh_key_pair_file&#39;</span><span class="p">]</span> <span class="c"># name of local file storing keypair</span></div><div class='line' id='LC62'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">key_name</span><span class="o">=</span><span class="n">Creds</span><span class="p">[</span><span class="s">&#39;ssh_key_name&#39;</span><span class="p">]</span>         <span class="c"># name of keypair on AWS</span></div><div class='line' id='LC63'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">security_groups</span><span class="o">=</span><span class="n">Creds</span><span class="p">[</span><span class="s">&#39;security_groups&#39;</span><span class="p">]</span> <span class="c"># security groups for controlling access</span></div><div class='line' id='LC64'><span class="k">except</span> <span class="ne">Exception</span><span class="p">,</span> <span class="n">e</span><span class="p">:</span></div><div class='line' id='LC65'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="n">e</span></div><div class='line' id='LC66'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">sys</span><span class="o">.</span><span class="n">exit</span><span class="p">(</span><span class="s">&#39;could not read credentials&#39;</span><span class="p">)</span></div><div class='line' id='LC67'><br/></div><div class='line' id='LC68'><span class="c"># open connection</span></div><div class='line' id='LC69'><span class="k">def</span> <span class="nf">open_connection</span><span class="p">(</span><span class="n">aws_access_key_id</span><span class="p">,</span></div><div class='line' id='LC70'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">aws_secret_access_key</span><span class="p">):</span></div><div class='line' id='LC71'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">conn</span> <span class="o">=</span> <span class="n">boto</span><span class="o">.</span><span class="n">ec2</span><span class="o">.</span><span class="n">connect_to_region</span><span class="p">(</span><span class="s">&quot;us-east-1&quot;</span><span class="p">,</span></div><div class='line' id='LC72'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">aws_access_key_id</span><span class="o">=</span><span class="n">aws_access_key_id</span><span class="p">,</span></div><div class='line' id='LC73'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">aws_secret_access_key</span><span class="o">=</span><span class="n">aws_secret_access_key</span><span class="p">)</span></div><div class='line' id='LC74'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&#39;Created Connection=&#39;</span><span class="p">,</span><span class="n">conn</span></div><div class='line' id='LC75'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">conn</span></div><div class='line' id='LC76'><br/></div><div class='line' id='LC77'><span class="c">#Get information about all current instances</span></div><div class='line' id='LC78'><span class="k">def</span> <span class="nf">report_all_instances</span><span class="p">():</span></div><div class='line' id='LC79'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">reservations</span> <span class="o">=</span> <span class="n">conn</span><span class="o">.</span><span class="n">get_all_instances</span><span class="p">()</span></div><div class='line' id='LC80'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">instances</span><span class="o">=</span><span class="p">[]</span></div><div class='line' id='LC81'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">count</span><span class="o">=</span><span class="mi">0</span></div><div class='line' id='LC82'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">instance_alive</span><span class="o">=-</span><span class="mi">1</span> <span class="c"># points to a pending or running instance, -1 indicates none</span></div><div class='line' id='LC83'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">pending</span><span class="o">=</span><span class="bp">True</span>     <span class="c"># indicates whether instance_alive refers to a pending instance.</span></div><div class='line' id='LC84'><br/></div><div class='line' id='LC85'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&#39;time: &#39;</span><span class="p">,</span><span class="n">time</span><span class="o">.</span><span class="n">strftime</span><span class="p">(</span><span class="s">&#39;%H:%M:%S&#39;</span><span class="p">)</span></div><div class='line' id='LC86'><br/></div><div class='line' id='LC87'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">reservation</span> <span class="ow">in</span> <span class="n">reservations</span><span class="p">:</span></div><div class='line' id='LC88'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&#39;</span><span class="se">\n</span><span class="s">Reservation: &#39;</span><span class="p">,</span><span class="n">reservation</span></div><div class='line' id='LC89'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">instance</span> <span class="ow">in</span> <span class="n">reservation</span><span class="o">.</span><span class="n">instances</span><span class="p">:</span></div><div class='line' id='LC90'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">instance</span><span class="o">.</span><span class="n">tags</span><span class="p">)</span><span class="o">==</span><span class="mi">2</span><span class="p">:</span></div><div class='line' id='LC91'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&#39;Instance tags=&#39;</span><span class="p">,</span><span class="n">instance</span><span class="o">.</span><span class="n">tags</span></div><div class='line' id='LC92'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC93'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&#39;instance no.=&#39;</span><span class="p">,</span><span class="n">count</span><span class="p">,</span><span class="s">&#39;instance name=&#39;</span><span class="p">,</span><span class="n">instance</span><span class="p">,</span><span class="s">&#39;DNS name = &#39;</span><span class="p">,</span><span class="n">instance</span><span class="o">.</span><span class="n">public_dns_name</span></div><div class='line' id='LC94'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&#39;Instance state=&#39;</span><span class="p">,</span><span class="n">instance</span><span class="o">.</span><span class="n">state</span></div><div class='line' id='LC95'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&#39;Instance tags=&#39;</span><span class="p">,</span><span class="nb">len</span><span class="p">(</span><span class="n">instance</span><span class="o">.</span><span class="n">tags</span><span class="p">)</span></div><div class='line' id='LC96'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&#39;This looks like a private instance launched by this script!&#39;</span></div><div class='line' id='LC97'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#This is the private instance, probably launched by this script.</span></div><div class='line' id='LC98'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">instance_alive</span><span class="o">==-</span><span class="mi">1</span> <span class="ow">and</span> <span class="n">instance</span><span class="o">.</span><span class="n">state</span> <span class="o">!=</span> <span class="s">&#39;terminated&#39;</span><span class="p">:</span></div><div class='line' id='LC99'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">instance</span><span class="o">.</span><span class="n">state</span> <span class="o">==</span><span class="s">&#39;running&#39;</span> <span class="ow">and</span> <span class="n">pending</span><span class="p">:</span></div><div class='line' id='LC100'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">instance_alive</span><span class="o">=</span><span class="n">count</span> <span class="c"># point to first running instance</span></div><div class='line' id='LC101'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">pending</span><span class="o">=</span><span class="bp">False</span></div><div class='line' id='LC102'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="n">instance</span><span class="o">.</span><span class="n">state</span> <span class="o">==</span><span class="s">&#39;pending&#39;</span> <span class="ow">and</span> <span class="n">pending</span><span class="p">:</span></div><div class='line' id='LC103'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">instance_alive</span><span class="o">=</span><span class="n">count</span> <span class="c"># point to first pending instance</span></div><div class='line' id='LC104'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&#39;ssh -i </span><span class="si">%s</span><span class="s"> </span><span class="si">%s</span><span class="s">@</span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">keyPairFile</span><span class="p">,</span><span class="n">login_id</span><span class="p">,</span><span class="n">instance</span><span class="o">.</span><span class="n">public_dns_name</span><span class="p">)</span></div><div class='line' id='LC105'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">instances</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">instance</span><span class="p">)</span></div><div class='line' id='LC106'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">count</span><span class="o">+=</span><span class="mi">1</span></div><div class='line' id='LC107'><br/></div><div class='line' id='LC108'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="p">(</span><span class="n">instances</span><span class="p">,</span><span class="n">instance_alive</span><span class="p">)</span></div><div class='line' id='LC109'><br/></div><div class='line' id='LC110'><span class="k">def</span> <span class="nf">emptyCallBack</span><span class="p">(</span><span class="n">line</span><span class="p">):</span> <span class="k">return</span> <span class="bp">False</span></div><div class='line' id='LC111'><br/></div><div class='line' id='LC112'><span class="k">def</span> <span class="nf">kill_all_notebooks</span><span class="p">():</span></div><div class='line' id='LC113'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">command</span><span class="o">=</span><span class="p">[</span><span class="s">&#39;scripts/CloseAllNotebooks.py&#39;</span><span class="p">]</span></div><div class='line' id='LC114'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">Send_Command</span><span class="p">(</span><span class="n">command</span><span class="p">,</span><span class="n">emptyCallBack</span><span class="p">)</span></div><div class='line' id='LC115'><br/></div><div class='line' id='LC116'><span class="k">def</span> <span class="nf">set_credentials</span><span class="p">():</span></div><div class='line' id='LC117'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot; set ID and secret key as environment variables on the remote machine&quot;&quot;&quot;</span></div><div class='line' id='LC118'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC119'><br/></div><div class='line' id='LC120'><span class="k">def</span> <span class="nf">copy_credentials</span><span class="p">(</span><span class="n">LocalDir</span><span class="p">):</span></div><div class='line' id='LC121'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="kn">from</span> <span class="nn">glob</span> <span class="kn">import</span> <span class="n">glob</span></div><div class='line' id='LC122'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&#39;Entered copy_credentials:&#39;</span><span class="p">,</span><span class="n">LocalDir</span></div><div class='line' id='LC123'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">mkdir</span><span class="o">=</span><span class="p">[</span><span class="s">&#39;mkdir&#39;</span><span class="p">,</span><span class="s">&#39;Vault&#39;</span><span class="p">]</span></div><div class='line' id='LC124'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">Send_Command</span><span class="p">(</span><span class="n">mkdir</span><span class="p">,</span><span class="n">emptyCallBack</span><span class="p">,</span><span class="n">dont_wait</span><span class="o">=</span><span class="bp">True</span><span class="p">)</span></div><div class='line' id='LC125'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">list</span><span class="o">=</span><span class="n">glob</span><span class="p">(</span><span class="n">args</span><span class="p">[</span><span class="s">&#39;Copy_Credentials&#39;</span><span class="p">])</span></div><div class='line' id='LC126'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">scp</span><span class="o">=</span><span class="p">[</span><span class="s">&#39;scp&#39;</span><span class="p">,</span><span class="s">&#39;-i&#39;</span><span class="p">,</span><span class="n">keyPairFile</span><span class="p">]</span><span class="o">+</span><span class="nb">list</span><span class="o">+</span><span class="p">[(</span><span class="s">&#39;</span><span class="si">%s</span><span class="s">@</span><span class="si">%s</span><span class="s">:Vault/&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">login_id</span><span class="p">,</span><span class="n">instance</span><span class="o">.</span><span class="n">public_dns_name</span><span class="p">))]</span></div><div class='line' id='LC127'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&#39; &#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">scp</span><span class="p">)</span></div><div class='line' id='LC128'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">subprocess</span><span class="o">.</span><span class="n">call</span><span class="p">(</span><span class="n">scp</span><span class="p">)</span></div><div class='line' id='LC129'><br/></div><div class='line' id='LC130'><span class="k">def</span> <span class="nf">set_password</span><span class="p">(</span><span class="n">password</span><span class="p">):</span></div><div class='line' id='LC131'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">password</span><span class="p">)</span><span class="o">&lt;</span><span class="mi">6</span><span class="p">:</span></div><div class='line' id='LC132'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">sys</span><span class="o">.</span><span class="n">exit</span><span class="p">(</span><span class="s">&#39;Password must be at least 6 characters long&#39;</span><span class="p">)</span></div><div class='line' id='LC133'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">command</span><span class="o">=</span><span class="p">[</span><span class="s">&quot;scripts/SetNotebookPassword.py&quot;</span><span class="p">,</span><span class="n">password</span><span class="p">]</span></div><div class='line' id='LC134'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">Send_Command</span><span class="p">(</span><span class="n">command</span><span class="p">,</span><span class="n">emptyCallBack</span><span class="p">)</span></div><div class='line' id='LC135'><br/></div><div class='line' id='LC136'><span class="k">def</span> <span class="nf">create_image</span><span class="p">(</span><span class="n">image_name</span><span class="p">):</span></div><div class='line' id='LC137'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#delete the Vault directory, where all of the secret keys and passwords reside.</span></div><div class='line' id='LC138'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">delete_Vault</span><span class="o">=</span><span class="p">[</span><span class="s">&#39;rm&#39;</span><span class="p">,</span><span class="s">&#39;-r&#39;</span><span class="p">,</span><span class="s">&#39;~/Vault&#39;</span><span class="p">]</span></div><div class='line' id='LC139'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">Send_Command</span><span class="p">(</span><span class="n">delete_Vault</span><span class="p">,</span><span class="n">emptyCallBack</span><span class="p">)</span></div><div class='line' id='LC140'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">instance</span><span class="o">.</span><span class="n">create_image</span><span class="p">(</span><span class="n">args</span><span class="p">[</span><span class="s">&#39;create_image&#39;</span><span class="p">])</span></div><div class='line' id='LC141'><br/></div><div class='line' id='LC142'><span class="k">def</span> <span class="nf">Send_Command</span><span class="p">(</span><span class="n">command</span><span class="p">,</span><span class="n">callback</span><span class="p">,</span><span class="n">dont_wait</span><span class="o">=</span><span class="bp">False</span><span class="p">):</span></div><div class='line' id='LC143'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">init</span><span class="o">=</span><span class="n">time</span><span class="o">.</span><span class="n">time</span><span class="p">()</span></div><div class='line' id='LC144'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC145'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&#39;SendCommand:&#39;</span><span class="p">,</span><span class="s">&#39; &#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">ssh</span><span class="o">+</span><span class="n">command</span><span class="p">)</span></div><div class='line' id='LC146'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">ssh_process</span> <span class="o">=</span> <span class="n">subprocess</span><span class="o">.</span><span class="n">Popen</span><span class="p">(</span><span class="n">ssh</span><span class="o">+</span><span class="n">command</span><span class="p">,</span></div><div class='line' id='LC147'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">shell</span><span class="o">=</span><span class="bp">False</span><span class="p">,</span></div><div class='line' id='LC148'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">stdin</span><span class="o">=</span><span class="n">subprocess</span><span class="o">.</span><span class="n">PIPE</span><span class="p">,</span></div><div class='line' id='LC149'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">stdout</span><span class="o">=</span><span class="n">subprocess</span><span class="o">.</span><span class="n">PIPE</span><span class="p">,</span></div><div class='line' id='LC150'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">stderr</span><span class="o">=</span><span class="n">subprocess</span><span class="o">.</span><span class="n">PIPE</span><span class="p">)</span></div><div class='line' id='LC151'><br/></div><div class='line' id='LC152'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">dataWaiting</span><span class="p">(</span><span class="n">source</span><span class="p">):</span></div><div class='line' id='LC153'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">select</span><span class="o">.</span><span class="n">select</span><span class="p">([</span><span class="n">source</span><span class="p">],</span> <span class="p">[],</span> <span class="p">[],</span> <span class="mi">0</span><span class="p">)</span> <span class="o">==</span> <span class="p">([</span><span class="n">source</span><span class="p">],</span> <span class="p">[],</span> <span class="p">[])</span></div><div class='line' id='LC154'><br/></div><div class='line' id='LC155'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">endReached</span><span class="o">=</span><span class="bp">False</span></div><div class='line' id='LC156'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">while</span> <span class="ow">not</span> <span class="n">endReached</span><span class="p">:</span></div><div class='line' id='LC157'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">dataWaiting</span><span class="p">(</span><span class="n">ssh_process</span><span class="o">.</span><span class="n">stdout</span><span class="p">):</span></div><div class='line' id='LC158'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">line</span><span class="o">=</span><span class="n">ssh_process</span><span class="o">.</span><span class="n">stdout</span><span class="o">.</span><span class="n">readline</span><span class="p">()</span></div><div class='line' id='LC159'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">line</span><span class="p">)</span><span class="o">&gt;</span><span class="mi">0</span><span class="p">:</span></div><div class='line' id='LC160'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="n">line</span><span class="p">,</span></div><div class='line' id='LC161'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC162'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">endReached</span> <span class="o">=</span> <span class="n">endReached</span> <span class="o">|</span> <span class="n">callback</span><span class="p">(</span><span class="n">line</span><span class="p">)</span></div><div class='line' id='LC163'><br/></div><div class='line' id='LC164'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">matchEnd</span><span class="o">=</span><span class="n">re</span><span class="o">.</span><span class="n">match</span><span class="p">(</span><span class="s">&#39;=== END ===&#39;</span><span class="p">,</span><span class="n">line</span><span class="p">)</span></div><div class='line' id='LC165'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">matchEnd</span><span class="p">:</span></div><div class='line' id='LC166'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">endReached</span><span class="o">=</span><span class="bp">True</span></div><div class='line' id='LC167'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">dont_wait</span><span class="p">:</span> <span class="n">endReached</span><span class="o">=</span><span class="bp">True</span></div><div class='line' id='LC168'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">time</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="mf">0.01</span><span class="p">)</span></div><div class='line' id='LC169'><br/></div><div class='line' id='LC170'><span class="k">def</span> <span class="nf">Launch_notebook</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s">&#39;&#39;</span><span class="p">):</span></div><div class='line' id='LC171'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">init</span><span class="o">=</span><span class="n">time</span><span class="o">.</span><span class="n">time</span><span class="p">()</span></div><div class='line' id='LC172'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC173'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">command</span><span class="o">=</span><span class="p">[</span><span class="s">&quot;scripts/launch_notebook.py&quot;</span><span class="p">,</span><span class="n">name</span><span class="p">,</span><span class="s">&quot;2&gt;&amp;1&quot;</span><span class="p">]</span></div><div class='line' id='LC174'><br/></div><div class='line' id='LC175'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">detect_launch_port</span><span class="p">(</span><span class="n">line</span><span class="p">):</span></div><div class='line' id='LC176'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">match</span><span class="o">=</span><span class="n">re</span><span class="o">.</span><span class="n">search</span><span class="p">(</span><span class="s">&#39;IPython\ Notebook\ is\ running\ at\:.*system\]\:(\d+)/&#39;</span><span class="p">,</span><span class="n">line</span><span class="p">)</span></div><div class='line' id='LC177'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">match</span><span class="p">:</span></div><div class='line' id='LC178'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">port_no</span><span class="o">=</span><span class="n">match</span><span class="o">.</span><span class="n">group</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span></div><div class='line' id='LC179'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&#39;opening https://&#39;</span><span class="o">+</span><span class="n">instance</span><span class="o">.</span><span class="n">public_dns_name</span><span class="o">+</span><span class="s">&#39;:&#39;</span><span class="o">+</span><span class="n">port_no</span><span class="o">+</span><span class="s">&#39;/&#39;</span></div><div class='line' id='LC180'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">webbrowser</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="s">&#39;https://&#39;</span><span class="o">+</span><span class="n">instance</span><span class="o">.</span><span class="n">public_dns_name</span><span class="o">+</span><span class="s">&#39;:&#39;</span><span class="o">+</span><span class="n">port_no</span><span class="o">+</span><span class="s">&#39;/&#39;</span><span class="p">)</span></div><div class='line' id='LC181'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">True</span></div><div class='line' id='LC182'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">False</span></div><div class='line' id='LC183'><br/></div><div class='line' id='LC184'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">Send_Command</span><span class="p">(</span><span class="n">command</span><span class="p">,</span><span class="n">detect_launch_port</span><span class="p">)</span></div><div class='line' id='LC185'><br/></div><div class='line' id='LC186'><br/></div><div class='line' id='LC187'><span class="k">if</span> <span class="n">__name__</span> <span class="o">==</span> <span class="s">&quot;__main__&quot;</span><span class="p">:</span></div><div class='line' id='LC188'><br/></div><div class='line' id='LC189'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># parse parameters</span></div><div class='line' id='LC190'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">parser</span> <span class="o">=</span> <span class="n">argparse</span><span class="o">.</span><span class="n">ArgumentParser</span><span class="p">(</span><span class="n">description</span><span class="o">=</span><span class="s">&#39;launch an ec2 instance and then start an ipython notebook server&#39;</span><span class="p">)</span></div><div class='line' id='LC191'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">parser</span><span class="o">.</span><span class="n">add_argument</span><span class="p">(</span><span class="s">&#39;-c&#39;</span><span class="p">,</span><span class="s">&#39;--collection&#39;</span><span class="p">,</span></div><div class='line' id='LC192'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">help</span><span class="o">=</span><span class="s">&quot;&quot;&quot;Choice of notebook collection, there are two options:</span></div><div class='line' id='LC193'><span class="s">                        1) &#39;@path&#39; an explicit path to the wanted directory, relative to /home/ubuntu</span><span class="se">\n\n</span><span class="s"></span></div><div class='line' id='LC194'><span class="s">                        2) &#39;name&#39; the name of a collection listed in the markdown file:</span><span class="se">\n\n</span><span class="s"></span></div><div class='line' id='LC195'><span class="s">                              https://github.com/yoavfreund/UCSD_BigData/blob/master/AWS_scripts/NotebookCollections.md</span><span class="se">\n\n</span><span class="s"></span></div><div class='line' id='LC196'><span class="s">                           the name of the collection is given in a pattern of the form __[name]__</span></div><div class='line' id='LC197'><span class="s">                        &quot;&quot;&quot;</span><span class="p">)</span></div><div class='line' id='LC198'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">parser</span><span class="o">.</span><span class="n">add_argument</span><span class="p">(</span><span class="s">&#39;-i&#39;</span><span class="p">,</span><span class="s">&#39;--create_image&#39;</span><span class="p">,</span></div><div class='line' id='LC199'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">help</span><span class="o">=</span><span class="s">&#39;Create an AMI from the current state of the (first) instance&#39;</span><span class="p">)</span></div><div class='line' id='LC200'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">parser</span><span class="o">.</span><span class="n">add_argument</span><span class="p">(</span><span class="s">&#39;-p&#39;</span><span class="p">,</span><span class="s">&#39;--password&#39;</span><span class="p">,</span></div><div class='line' id='LC201'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">help</span><span class="o">=</span><span class="s">&#39;Specify password for notebook (if missing=use existing password)&#39;</span><span class="p">)</span></div><div class='line' id='LC202'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">parser</span><span class="o">.</span><span class="n">add_argument</span><span class="p">(</span><span class="s">&#39;-t&#39;</span><span class="p">,</span><span class="s">&#39;--instance_type&#39;</span><span class="p">,</span><span class="n">default</span><span class="o">=</span><span class="s">&#39;t1.micro&#39;</span><span class="p">,</span></div><div class='line' id='LC203'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">help</span><span class="o">=</span><span class="s">&#39;Type of instance to launch, Common choices are t1.micro,c1.medium,m3.xlarge, for more info see: https://aws.amazon.com//ec2/instance-types/&#39;</span><span class="p">)</span></div><div class='line' id='LC204'><span class="c">#Some common choices:</span></div><div class='line' id='LC205'><span class="c">#              vCPU     ECU	Memory (GiB)	Instance Storage (GB)	Linux/UNIX Usage</span></div><div class='line' id='LC206'><span class="c">#----------------------------------------------------------------------------------------</span></div><div class='line' id='LC207'><span class="c">#t1.micro	1	Variable    0.615	 EBS Only	        $0.020 per Hour</span></div><div class='line' id='LC208'><span class="c">#c1.medium	2	5	    1.7	         1 x 350	        $0.145 per Hour</span></div><div class='line' id='LC209'><span class="c">#m3.xlarge	4	13	    15	         2 x 40 SSD	        $0.450 per Hour</span></div><div class='line' id='LC210'><span class="c">#----------------------------------------------------------------------------------------</span></div><div class='line' id='LC211'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">parser</span><span class="o">.</span><span class="n">add_argument</span><span class="p">(</span><span class="s">&#39;-k&#39;</span><span class="p">,</span><span class="s">&#39;--kill_all&#39;</span><span class="p">,</span><span class="n">dest</span><span class="o">=</span><span class="s">&#39;kill&#39;</span><span class="p">,</span><span class="n">action</span><span class="o">=</span><span class="s">&#39;store_true&#39;</span><span class="p">,</span><span class="n">default</span><span class="o">=</span><span class="bp">False</span><span class="p">,</span></div><div class='line' id='LC212'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">help</span><span class="o">=</span><span class="s">&#39;close all running notebook servers&#39;</span><span class="p">)</span></div><div class='line' id='LC213'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">parser</span><span class="o">.</span><span class="n">add_argument</span><span class="p">(</span><span class="s">&#39;-d&#39;</span><span class="p">,</span><span class="s">&#39;--disk_size&#39;</span><span class="p">,</span> <span class="n">default</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="nb">type</span><span class="o">=</span><span class="nb">int</span><span class="p">,</span></div><div class='line' id='LC214'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">help</span><span class="o">=</span><span class="s">&#39;Amount of additional disk space in GB (default 0)&#39;</span><span class="p">)</span></div><div class='line' id='LC215'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">parser</span><span class="o">.</span><span class="n">add_argument</span><span class="p">(</span><span class="s">&#39;-A&#39;</span><span class="p">,</span><span class="s">&#39;--Copy_Credentials&#39;</span><span class="p">,</span></div><div class='line' id='LC216'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">help</span><span class="o">=</span><span class="s">&#39;Copy the credentials files to the Vault directory on the AWS instance. Parameter is a the full path of the files you want to transfer to the vault. Wildcards are allowed but have to be preceded by a &quot;</span><span class="se">\&quot;</span><span class="s">)&#39;</span><span class="p">)</span></div><div class='line' id='LC217'><br/></div><div class='line' id='LC218'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">args</span> <span class="o">=</span> <span class="nb">vars</span><span class="p">(</span><span class="n">parser</span><span class="o">.</span><span class="n">parse_args</span><span class="p">())</span></div><div class='line' id='LC219'><br/></div><div class='line' id='LC220'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># print &#39;args=&#39;,args</span></div><div class='line' id='LC221'><br/></div><div class='line' id='LC222'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># open connection to aws</span></div><div class='line' id='LC223'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&#39;The regions you are connected to are:&#39;</span><span class="p">,</span><span class="n">boto</span><span class="o">.</span><span class="n">ec2</span><span class="o">.</span><span class="n">regions</span><span class="p">()</span></div><div class='line' id='LC224'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC225'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">conn</span><span class="o">=</span><span class="n">open_connection</span><span class="p">(</span><span class="n">aws_access_key_id</span><span class="p">,</span><span class="n">aws_secret_access_key</span><span class="p">)</span></div><div class='line' id='LC226'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">except</span><span class="p">:</span></div><div class='line' id='LC227'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">e</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">exc_info</span><span class="p">()[</span><span class="mi">0</span><span class="p">]</span></div><div class='line' id='LC228'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&quot;Error: </span><span class="si">%s</span><span class="s">&quot;</span> <span class="o">%</span> <span class="n">e</span></div><div class='line' id='LC229'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">sys</span><span class="o">.</span><span class="n">exit</span><span class="p">(</span><span class="s">&quot;failed to connect to AWS&quot;</span><span class="p">)</span></div><div class='line' id='LC230'><br/></div><div class='line' id='LC231'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#Get and print information about all current instances</span></div><div class='line' id='LC232'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">login_id</span><span class="o">=</span><span class="s">&#39;ubuntu&#39;</span></div><div class='line' id='LC233'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">(</span><span class="n">instances</span><span class="p">,</span><span class="n">instance_alive</span><span class="p">)</span> <span class="o">=</span> <span class="n">report_all_instances</span><span class="p">()</span></div><div class='line' id='LC234'><br/></div><div class='line' id='LC235'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">instance_alive</span><span class="o">==-</span><span class="mi">1</span><span class="p">:</span> <span class="c"># if there is no instance that is pending or running, create one</span></div><div class='line' id='LC236'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">instance_type</span><span class="o">=</span><span class="n">args</span><span class="p">[</span><span class="s">&#39;instance_type&#39;</span><span class="p">]</span></div><div class='line' id='LC237'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">disk_size</span><span class="o">=</span><span class="n">args</span><span class="p">[</span><span class="s">&#39;disk_size&#39;</span><span class="p">]</span></div><div class='line' id='LC238'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&#39;launching an ec2 instance, instance type=&#39;</span><span class="p">,</span><span class="n">instance_type</span><span class="p">,</span><span class="s">&#39;, ami=&#39;</span><span class="p">,</span><span class="n">ami</span><span class="p">,</span><span class="s">&#39;, disk size=&#39;</span><span class="p">,</span><span class="n">disk_size</span></div><div class='line' id='LC239'><br/></div><div class='line' id='LC240'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">bdm</span> <span class="o">=</span> <span class="n">boto</span><span class="o">.</span><span class="n">ec2</span><span class="o">.</span><span class="n">blockdevicemapping</span><span class="o">.</span><span class="n">BlockDeviceMapping</span><span class="p">()</span></div><div class='line' id='LC241'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">disk_size</span><span class="o">&gt;</span><span class="mi">0</span><span class="p">:</span></div><div class='line' id='LC242'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dev_sda1</span> <span class="o">=</span> <span class="n">boto</span><span class="o">.</span><span class="n">ec2</span><span class="o">.</span><span class="n">blockdevicemapping</span><span class="o">.</span><span class="n">EBSBlockDeviceType</span><span class="p">()</span></div><div class='line' id='LC243'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dev_sda1</span><span class="o">.</span><span class="n">size</span> <span class="o">=</span> <span class="n">disk_size</span> <span class="c"># size in Gigabytes</span></div><div class='line' id='LC244'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">bdm</span><span class="p">[</span><span class="s">&#39;/dev/sda1&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">dev_sda1</span> </div><div class='line' id='LC245'><br/></div><div class='line' id='LC246'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">reservation</span><span class="o">=</span><span class="n">conn</span><span class="o">.</span><span class="n">run_instances</span><span class="p">(</span><span class="n">ami</span><span class="p">,</span></div><div class='line' id='LC247'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">key_name</span><span class="o">=</span><span class="n">key_name</span><span class="p">,</span></div><div class='line' id='LC248'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">instance_type</span><span class="o">=</span><span class="n">instance_type</span><span class="p">,</span></div><div class='line' id='LC249'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">security_groups</span><span class="o">=</span><span class="n">security_groups</span><span class="p">,</span></div><div class='line' id='LC250'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">block_device_map</span> <span class="o">=</span> <span class="n">bdm</span><span class="p">)</span></div><div class='line' id='LC251'><br/></div><div class='line' id='LC252'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&#39;Launched Instance&#39;</span><span class="p">,</span><span class="n">reservation</span></div><div class='line' id='LC253'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC254'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">(</span><span class="n">instances</span><span class="p">,</span><span class="n">instance_alive</span><span class="p">)</span> <span class="o">=</span> <span class="n">report_all_instances</span><span class="p">()</span></div><div class='line' id='LC255'><br/></div><div class='line' id='LC256'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># choose an instance and check that it is running</span></div><div class='line' id='LC257'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">instance</span> <span class="o">=</span> <span class="n">instances</span><span class="p">[</span><span class="n">instance_alive</span><span class="p">]</span></div><div class='line' id='LC258'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">while</span> <span class="n">instance</span><span class="o">.</span><span class="n">state</span> <span class="o">!=</span> <span class="s">&#39;running&#39;</span><span class="p">:</span></div><div class='line' id='LC259'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&#39;</span><span class="se">\r</span><span class="s">&#39;</span><span class="p">,</span><span class="n">time</span><span class="o">.</span><span class="n">strftime</span><span class="p">(</span><span class="s">&#39;%H:%M:%S&#39;</span><span class="p">),</span><span class="n">instance</span><span class="o">.</span><span class="n">state</span><span class="p">,</span></div><div class='line' id='LC260'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">time</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="mi">5</span><span class="p">)</span></div><div class='line' id='LC261'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&#39;</span><span class="se">\n</span><span class="s"> Instance Ready!&#39;</span><span class="p">,</span><span class="n">time</span><span class="o">.</span><span class="n">strftime</span><span class="p">(</span><span class="s">&#39;%H:%M:%S&#39;</span><span class="p">),</span><span class="n">instance</span><span class="o">.</span><span class="n">state</span></div><div class='line' id='LC262'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">ssh</span><span class="o">=</span><span class="p">[</span><span class="s">&#39;ssh&#39;</span><span class="p">,</span><span class="s">&#39;-i&#39;</span><span class="p">,</span><span class="n">keyPairFile</span><span class="p">,(</span><span class="s">&#39;</span><span class="si">%s</span><span class="s">@</span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">login_id</span><span class="p">,</span><span class="n">instance</span><span class="o">.</span><span class="n">public_dns_name</span><span class="p">))]</span></div><div class='line' id='LC263'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&quot;To connect to instance, use:</span><span class="se">\n</span><span class="s">&quot;</span><span class="p">,</span><span class="s">&#39; &#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">ssh</span><span class="p">)</span></div><div class='line' id='LC264'><br/></div><div class='line' id='LC265'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span><span class="p">(</span><span class="n">args</span><span class="p">[</span><span class="s">&#39;password&#39;</span><span class="p">]</span> <span class="o">!=</span> <span class="bp">None</span><span class="p">):</span></div><div class='line' id='LC266'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">set_password</span><span class="p">(</span><span class="n">args</span><span class="p">[</span><span class="s">&#39;password&#39;</span><span class="p">])</span></div><div class='line' id='LC267'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC268'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span><span class="p">(</span><span class="n">args</span><span class="p">[</span><span class="s">&#39;kill&#39;</span><span class="p">]):</span></div><div class='line' id='LC269'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&quot;closing all notebook servers&quot;</span></div><div class='line' id='LC270'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">kill_all_notebooks</span><span class="p">()</span></div><div class='line' id='LC271'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">sys</span><span class="o">.</span><span class="n">exit</span><span class="p">()</span></div><div class='line' id='LC272'><br/></div><div class='line' id='LC273'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span><span class="p">(</span><span class="n">args</span><span class="p">[</span><span class="s">&#39;collection&#39;</span><span class="p">]</span> <span class="o">!=</span> <span class="bp">None</span><span class="p">):</span></div><div class='line' id='LC274'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">Launch_notebook</span><span class="p">(</span><span class="n">args</span><span class="p">[</span><span class="s">&#39;collection&#39;</span><span class="p">])</span></div><div class='line' id='LC275'><br/></div><div class='line' id='LC276'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span><span class="p">(</span><span class="n">args</span><span class="p">[</span><span class="s">&#39;create_image&#39;</span><span class="p">]</span> <span class="o">!=</span> <span class="bp">None</span><span class="p">):</span></div><div class='line' id='LC277'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&quot;creating a new AMI called&quot;</span><span class="p">,</span><span class="n">args</span><span class="p">[</span><span class="s">&#39;create_image&#39;</span><span class="p">]</span></div><div class='line' id='LC278'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">create_image</span><span class="p">(</span><span class="n">args</span><span class="p">[</span><span class="s">&#39;create_image&#39;</span><span class="p">])</span></div><div class='line' id='LC279'><br/></div><div class='line' id='LC280'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span><span class="p">(</span><span class="n">args</span><span class="p">[</span><span class="s">&#39;Copy_Credentials&#39;</span><span class="p">]</span><span class="o">!=</span> <span class="bp">None</span><span class="p">):</span></div><div class='line' id='LC281'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">copy_credentials</span><span class="p">(</span><span class="n">args</span><span class="p">[</span><span class="s">&#39;Copy_Credentials&#39;</span><span class="p">])</span></div><div class='line' id='LC282'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC283'><br/></div></pre></div></td>
          </tr>
        </table>
  </div>

  </div>
</div>

<a href="#jump-to-line" rel="facebox[.linejump]" data-hotkey="l" class="js-jump-to-line" style="display:none">Jump to Line</a>
<div id="jump-to-line" style="display:none">
  <form accept-charset="UTF-8" class="js-jump-to-line-form">
    <input class="linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" autofocus>
    <button type="submit" class="button">Go</button>
  </form>
</div>

        </div>

      </div><!-- /.repo-container -->
      <div class="modal-backdrop"></div>
    </div><!-- /.container -->
  </div><!-- /.site -->


    </div><!-- /.wrapper -->

      <div class="container">
  <div class="site-footer">
    <ul class="site-footer-links right">
      <li><a href="https://status.github.com/">Status</a></li>
      <li><a href="http://developer.github.com">API</a></li>
      <li><a href="http://training.github.com">Training</a></li>
      <li><a href="http://shop.github.com">Shop</a></li>
      <li><a href="/blog">Blog</a></li>
      <li><a href="/about">About</a></li>

    </ul>

    <a href="/">
      <span class="mega-octicon octicon-mark-github" title="GitHub"></span>
    </a>

    <ul class="site-footer-links">
      <li>&copy; 2014 <span title="0.09294s from github-fe121-cp1-prd.iad.github.net">GitHub</span>, Inc.</li>
        <li><a href="/site/terms">Terms</a></li>
        <li><a href="/site/privacy">Privacy</a></li>
        <li><a href="/security">Security</a></li>
        <li><a href="/contact">Contact</a></li>
    </ul>
  </div><!-- /.site-footer -->
</div><!-- /.container -->


    <div class="fullscreen-overlay js-fullscreen-overlay" id="fullscreen_overlay">
  <div class="fullscreen-container js-fullscreen-container">
    <div class="textarea-wrap">
      <textarea name="fullscreen-contents" id="fullscreen-contents" class="fullscreen-contents js-fullscreen-contents" placeholder="" data-suggester="fullscreen_suggester"></textarea>
    </div>
  </div>
  <div class="fullscreen-sidebar">
    <a href="#" class="exit-fullscreen js-exit-fullscreen tooltipped tooltipped-w" aria-label="Exit Zen Mode">
      <span class="mega-octicon octicon-screen-normal"></span>
    </a>
    <a href="#" class="theme-switcher js-theme-switcher tooltipped tooltipped-w"
      aria-label="Switch themes">
      <span class="octicon octicon-color-mode"></span>
    </a>
  </div>
</div>



    <div id="ajax-error-message" class="flash flash-error">
      <span class="octicon octicon-alert"></span>
      <a href="#" class="octicon octicon-remove-close close js-ajax-error-dismiss"></a>
      Something went wrong with that request. Please try again.
    </div>


      <script crossorigin="anonymous" src="https://assets-cdn.github.com/assets/frameworks-5a921ce2c45d4a5235b8f9c5c716611df0a83a79.js" type="text/javascript"></script>
      <script async="async" crossorigin="anonymous" src="https://assets-cdn.github.com/assets/github-8433b2222746cb6b0612174c45ef4b10522ff40c.js" type="text/javascript"></script>
      
      
  </body>
</html>

