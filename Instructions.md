# Prompt Instructions

---

Please convert this CSV of Bookmarks to a structured markdown file. I will provide you examples and give you directions on how to format and structure. The csv file has 7 columns.

- boldtitle = **Title In Bold**
- cover = ![]() an image url 
- title = [Title]
- url = (url)
- excerpt = - description 
- created = Date: 
- tags = Tags: #tags if multiple tags appear add a # in front of each #word

Below is an example of how the csv looks.

boldtitle,cover,title,url,excerpt,created,tags	
**AiTerm**	https://www.aiterm.net/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fmainfeat.905b7ea2.gif&w=1200&q=75	AiTerm	https://www.aiterm.net/	Your AI Terminal Assistant	2023-12-15T20:39:28.511Z	#ai #terminal

I want you to restructure this to look like the example below:

**AiTerm**	

![](https://www.aiterm.net/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fmainfeat.905b7ea2.gif&w=1200&q=75)

- [AiTerm](https://www.aiterm.net/) - Your AI Terminal Assistant	

**Date:** 2023-12-15T20:39:28.511Z
**Tags:** #ai #terminal

---

This Structure is called a block and heres how we do it.

{boldtitle}
{empty line}
{cover} 
{empty line}
{title}{url}{excerpt}- [title](url) - excerpt goes here.
{empty line}
{created} **Date:** 
{tags} **Tags:** 
{empty line}

---

Do you understand? If so please format into a markdown file called 12-23.md