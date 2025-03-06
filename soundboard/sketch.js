let width = window.innerWidth;
let height = window.innerHeight;

let buttons_top = [];
let buttons_middle = [];
let buttons_bottom = [];

let vine_boom;
let retro_game;
let whoosh;
let acute_guitar;
let guitar_string;
let guitar_notif;

function setup() {
  canvas = createCanvas(width,height);
  fog_horn = loadSound('fog_horn.mp3');
  womp = loadSound('womp.mp3');
  you_what_spongebob = loadSound('you_what_spongebob.mp3');
  myleg = loadSound('myleg.mp3');
  fail = loadSound('fail.mp3');
  dissapointed = loadSound('dissapointed.mp3');
  bee_boo_boo_bop = loadSound('bee_boo_boo_bop.mp3');
  lesson = loadSound('lesson.mp3');
  oh_brother = loadSound('oh_brother.mp3');

  let b1 = new Button(width/3, height/3, 200, 80, color(226, 132, 19), color(244, 190, 124), fog_horn);
  let b2 = new Button(width/2, height/3, 200, 80, color(0, 159, 183), color(153, 241, 255), womp);
  let b3 = new Button(2*width/3, height/3, 200, 80, color(145, 145, 233), color(204, 204, 245), you_what_spongebob);

  let b4 = new Button(width/3, height/2, 200, 80, color(205,92,92), color(240,128,128), myleg);
  let b5 = new Button(width/2, height/2, 200, 80, color(72,209,204), color(175,238,238), fail);
  let b6 = new Button(2*width/3, height/2, 200, 80, color(255,215,0), color(255,255,0), dissapointed);

  let b7 = new Button(width/3, 2*height/3, 200, 80, color(255, 163, 175), color(255, 214, 220), bee_boo_boo_bop);
  let b8 = new Button(width/2, 2*height/3, 200, 80, color(143, 45, 86), color(216, 131, 166), lesson);
  let b9 = new Button(2*width/3, 2*height/3, 200, 80, color(236, 78, 32), color(234, 162, 133), oh_brother);

  buttons_top.push(b1);
  buttons_top.push(b2);
  buttons_top.push(b3);

  buttons_middle.push(b4);
  buttons_middle.push(b5);
  buttons_middle.push(b6);

  buttons_bottom.push(b7);
  buttons_bottom.push(b8);
  buttons_bottom.push(b9);
}

function mousePressed() {
  for (let i = 0; i < buttons_top.length; i++) {
    buttons_top[i].clicked(mouseX, mouseY);
    buttons_middle[i].clicked(mouseX, mouseY);
    buttons_bottom[i].clicked(mouseX, mouseY);
  }
}

function mouseReleased() {
  for (let i = 0; i < buttons_top.length; i++) {
    buttons_top[i].y = height/3;
    buttons_middle[i].y = height/2;
    buttons_bottom[i].y = 2*height/3;
  }
}

function draw() {
  background(51, 92, 129);
  noStroke();
  for (let i = 0; i < buttons_top.length; i++) {
    buttons_top[i].show(); // using our show function from our Button class.
    buttons_middle[i].show();
    buttons_bottom[i].show();
  }
}

class Button {
  constructor(x, y, w, h, color, accent, sound) {
    this.x = x;
    this.y = y;
    this.w = w;
    this.h = h;
    this.color = color;
    this.accent = accent;
    this.sound = sound;
  }

  show() {
    noStroke();
    fill(this.color);
    rect((this.x - 100), this.y, this.w, 50);

    fill(this.accent);
    ellipse(this.x, this.y, this.w, this.h);

    fill(this.color);
    arc(this.x, (this.y + 50), this.w, this.h, TWO_PI, PI);
  }

  clicked(px, py) {
    let d = dist(px, py, this.x, this.y);

    if (d < this.w / 2) {
      this.y = this.y + 10;
      this.sound.play();
    } 
  }
}