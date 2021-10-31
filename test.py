import requests
from bs4 import BeautifulSoup

url = "https://readcomiconline.li/"


page = requests.get(url)
soup = BeautifulSoup(page.content, "lxml")

# print(soup.prettify()) # this part works as expected

res = soup.find("div", class_="search_box")

search_input = "batman"

print(page.json())

# print(res.prettify())
"""
<div class="search_box">
 <form action="/Search/Comic" method="post">
  <input name="keyword" type="text"/>
  <input type="submit" value=""/>
 </form>
</div>

"""


"""
<div id="tab-newest">
    <div style="position:relative"><a href="Comic/Hell-Baby"><img width="80px" height="100px" src="/Uploads/Etc/5-1-2021/98494843071267.jpg"></a><a class="title" href="Comic/Hell-Baby"><span>Hell Baby</span></a><p><span class="info">Genres:</span>&nbsp;<a href="/Genre/Graphic-Novels" class="dotUnder" title=".">Graphic Novels</a><span class="info">,</span> <a href="/Genre/Horror" class="dotUnder" title=".">Horror</a></p><p><span class="info">Latest:</span>&nbsp;<a href="/Comic/Hell-Baby/TPB-Part-2?id=184121" title="Watch Hell Baby TPB (Part 2) online">TPB (Part 2)</a></p><div style="position:absolute;top:0px; left:680px; width:28px; height:28px"><img src="../../Content/images/numbers/1.png"></div></div><div style="position:relative" class="blue"><a href="Comic/Lullabies-From-Hell"><img width="80px" height="100px" src="/Uploads/Etc/5-1-2021/71990743071266.jpg"></a><a class="title" href="Comic/Lullabies-From-Hell"><span>Lullabies From Hell</span></a><p><span class="info">Genres:</span>&nbsp;<a href="/Genre/Biography" class="dotUnder" title=".">Biography</a><span class="info">,</span> <a href="/Genre/Fantasy" class="dotUnder" title=".">Fantasy</a></p><p><span class="info">Latest:</span>&nbsp;<a href="/Comic/Lullabies-From-Hell/TPB-Part-2?id=184119" title="Watch Lullabies From Hell TPB (Part 2) online">TPB (Part 2)</a></p><div style="position: absolute; top: 0px; left: 680px; width: 28px; height: 28px; background-color: rgb(22, 22, 22); --darkreader-inline-bgcolor:#131415;" data-darkreader-inline-bgcolor=""><img src="../../Content/images/numbers/2.png"></div></div><div style="position:relative"><a href="Comic/Probe"><img width="80px" height="100px" src="/Uploads/Etc/5-1-2021/86965043071265.jpg"></a><a class="title" href="Comic/Probe"><span>Probe</span></a><p><span class="info">Genres:</span>&nbsp;<a href="/Genre/Superhero" class="dotUnder" title=".">Superhero</a><span class="info">,</span> <a href="/Genre/Action" class="dotUnder" title=".">Action</a><span class="info">,</span> <a href="/Genre/Adventure" class="dotUnder" title=".">Adventure</a></p><p><span class="info">Latest:</span>&nbsp;<a href="/Comic/Probe/Issue-1?id=184117" title="Watch Probe Issue #1 online">Issue #1</a></p><div style="position:absolute;top:0px; left:680px; width:28px; height:28px"><img src="../../Content/images/numbers/3.png"></div></div><div style="position:relative" class="blue"><a href="Comic/Nazrat"><img width="80px" height="100px" src="/Uploads/Etc/5-1-2021/95094243071264.jpg"></a><a class="title" href="Comic/Nazrat"><span>Nazrat</span></a><p><span class="info">Genres:</span>&nbsp;<a href="/Genre/Action" class="dotUnder" title=".">Action</a><span class="info">,</span> <a href="/Genre/Adventure" class="dotUnder" title=".">Adventure</a><span class="info">,</span> <a href="/Genre/Superhero" class="dotUnder" title=".">Superhero</a></p><p><span class="info">Latest:</span>&nbsp;<a href="/Comic/Nazrat/Issue-3?id=184116" title="Watch Nazrat Issue #3 online">Issue #3</a></p><div style="position: absolute; top: 0px; left: 680px; width: 28px; height: 28px; background-color: rgb(22, 22, 22); --darkreader-inline-bgcolor:#131415;" data-darkreader-inline-bgcolor=""><img src="../../Content/images/numbers/4.png"></div></div><div style="position:relative"><a href="Comic/The-Forbidden-Harbor"><img width="80px" height="100px" src="/Uploads/Etc/5-1-2021/9368043071263.jpg"></a><a class="title" href="Comic/The-Forbidden-Harbor"><span>The Forbidden Harbor</span></a><p><span class="info">Genres:</span>&nbsp;<a href="/Genre/Graphic-Novels" class="dotUnder" title=".">Graphic Novels</a></p><p><span class="info">Latest:</span>&nbsp;<a href="/Comic/The-Forbidden-Harbor/TPB-Part-3?id=184115" title="Watch The Forbidden Harbor TPB (Part 3) online">TPB (Part 3)</a></p><div style="position:absolute;top:0px; left:680px; width:28px; height:28px"><img src="../../Content/images/numbers/5.png"></div></div><div style="position:relative" class="blue"><a href="Comic/Macedonia"><img width="80px" height="100px" src="/Uploads/Etc/5-1-2021/91160343071262.jpg"></a><a class="title" href="Comic/Macedonia"><span>Macedonia</span></a><p><span class="info">Genres:</span>&nbsp;<a href="/Genre/Mature" class="dotUnder" title=".">Mature</a></p><p><span class="info">Latest:</span>&nbsp;<a href="/Comic/Macedonia/TPB-Part-2?id=184112" title="Watch Macedonia TPB (Part 2) online">TPB (Part 2)</a></p><div style="position: absolute; top: 0px; left: 680px; width: 28px; height: 28px; background-color: rgb(22, 22, 22); --darkreader-inline-bgcolor:#131415;" data-darkreader-inline-bgcolor=""><img src="../../Content/images/numbers/6.png"></div></div><div style="position:relative"><a href="Comic/Grimm-Universe-Presents-Quarterly-Steampunk"><img width="80px" height="100px" src="/Uploads/Etc/5-1-2021/48501943071261.jpg"></a><a class="title" href="Comic/Grimm-Universe-Presents-Quarterly-Steampunk"><span>Grimm Universe Presents Quarterly: Steampunk</span></a><p><span class="info">Genres:</span>&nbsp;<a href="/Genre/Action" class="dotUnder" title=".">Action</a><span class="info">,</span> <a href="/Genre/Adventure" class="dotUnder" title=".">Adventure</a><span class="info">,</span> <a href="/Genre/Fantasy" class="dotUnder" title=".">Fantasy</a><span class="info">,</span> <a href="/Genre/Horror" class="dotUnder" title=".">Horror</a></p><p><span class="info">Latest:</span>&nbsp;<a href="/Comic/Grimm-Universe-Presents-Quarterly-Steampunk/TPB?id=184110" title="Watch Grimm Universe Presents Quarterly: Steampunk TPB online">TPB</a></p><div style="position:absolute;top:0px; left:680px; width:28px; height:28px"><img src="../../Content/images/numbers/7.png"></div></div><div style="position:relative" class="blue"><a href="Comic/The-Bug-Boy"><img width="80px" height="100px" src="/Uploads/Etc/4-30-2021/59463843071260.jpg"></a><a class="title" href="Comic/The-Bug-Boy"><span>The Bug Boy</span></a><p><span class="info">Genres:</span>&nbsp;<a href="/Genre/Horror" class="dotUnder" title=".">Horror</a></p><p><span class="info">Latest:</span>&nbsp;<a href="/Comic/The-Bug-Boy/TPB-Part-2?id=184107" title="Watch The Bug Boy TPB (Part 2) online">TPB (Part 2)</a></p><div style="position: absolute; top: 0px; left: 680px; width: 28px; height: 28px; background-color: rgb(22, 22, 22); --darkreader-inline-bgcolor:#131415;" data-darkreader-inline-bgcolor=""><img src="../../Content/images/numbers/8.png"></div></div><div style="position:relative"><a href="Comic/Marx-Freud-Einstein-Heroes-of-the-Mind"><img width="80px" height="100px" src="/Uploads/Etc/4-30-2021/68270043071259.jpg"></a><a class="title" href="Comic/Marx-Freud-Einstein-Heroes-of-the-Mind"><span>Marx, Freud &amp; Einstein: Heroes of the Mind</span></a><p><span class="info">Genres:</span>&nbsp;<a href="/Genre/Graphic-Novels" class="dotUnder" title=".">Graphic Novels</a></p><p><span class="info">Latest:</span>&nbsp;<a href="/Comic/Marx-Freud-Einstein-Heroes-of-the-Mind/TPB-Part-2?id=184106" title="Watch Marx, Freud &amp; Einstein: Heroes of the Mind TPB (Part 2) online">TPB (Part 2)</a></p><div style="position:absolute;top:0px; left:680px; width:28px; height:28px"><img src="../../Content/images/numbers/9.png"></div></div><div style="position:relative" class="blue"><a href="Comic/Mean-Girls-Club-Pink-Dawn"><img width="80px" height="100px" src="/Uploads/Etc/4-30-2021/76558343071258.jpg"></a><a class="title" href="Comic/Mean-Girls-Club-Pink-Dawn"><span>Mean Girls Club: Pink Dawn</span></a><p><span class="info">Genres:</span>&nbsp;<a href="/Genre/Graphic-Novels" class="dotUnder" title=".">Graphic Novels</a></p><p><span class="info">Latest:</span>&nbsp;<a href="/Comic/Mean-Girls-Club-Pink-Dawn/TPB?id=184103" title="Watch Mean Girls Club: Pink Dawn TPB online">TPB</a></p><div style="position: absolute; top: 0px; left: 680px; width: 28px; height: 28px; background-color: rgb(22, 22, 22); --darkreader-inline-bgcolor:#131415;" data-darkreader-inline-bgcolor=""><img src="../../Content/images/numbers/10.png"></div></div>
        <div style="text-align: right; font-size: 16px">
            <a class="red" href="/ComicList/Newest">More...</a>
        </div>
    </div>
"""