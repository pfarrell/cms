// reimplementation of falling sand demo from https://jason.today/falling-sand using Canvas directly instead of p5.js
// copywrite 2022 Patrick Farrell
// created: 2022-08-29

class Grid {
  constructor(width, height, pixelSize=5) {
    this.width = width;
    this.height = height;
    this.pixelSize = pixelSize;
    this.scaledWidth = Math.floor(this.width / this.pixelSize);
    this.scaledHeight= Math.floor(this.height/ this.pixelSize);
    // bitmap simplifies the canvas so we can have pixels of arbitrary size
    this.bitmap= new Array(this.scaledWidth * this.scaledHeight).fill(0);
  }

  // Allow us to clear the canvas
  clear() {
    this.bitmap= new Array(this.scaledWidth * this.scaledHeight).fill(0);
  }

  // returns a map of the raw pixel location to the pixel grid
  loc(val) {
    return Math.floor(val / this.pixelSize);
  }

  // returns the pixel grid array index for a raw x, y location on the canvas
  idx(x, y) {
    return this.loc(x) + this.loc(y) * this.scaledWidth;
  }

  // Allow us to set a specific particle
  set(x, y, color) {
    if(this.isEmpty(this.idx(x, y))) {
      this.bitmap[this.idx(x, y)] = color;
    }
  }

  get(x, y) {
    return this.bitmap[this.idx(x, y)];
  }

  // Allow us to swap two particles (or space)
  swap(a, b) {
    const temp = this.bitmap[a];
    this.bitmap[a] = this.bitmap[b];
    this.bitmap[b] = temp;
  }

  isEmpty(idx) {
    return this.bitmap[idx] === 0;
  }

  updatePixel(i) {
    let below = i + this.scaledWidth;
    let belowLeft = below - 1;
    let belowRight = below + 1;
    if(this.isEmpty(below)) {
      this.swap(i, below);
    } else if (this.isEmpty(belowRight)) {
      this.swap(i, belowRight);
    } else if (this.isEmpty(belowLeft)) {
      this.swap(i, belowLeft);
    }
  }

  update() {
    for(let i=this.bitmap.length - this.scaledWidth - 1; i > 0; i--) {
      this.updatePixel(i);
    }
  }
}

function imgDataToCoord(p, imgWidth) {
  let pFloor = Math.floor(p/4);
  let xPos = pFloor % imgWidth;
  let yPos = (pFloor - xPos) / imgWidth ;
  return { x: xPos, y: yPos };
}

function getMousePos(evt) {
  const rect = evt.target.getBoundingClientRect();
  return { x: Math.round(evt.clientX - rect.left), y: Math.round(evt.clientY - rect.top) };
}

function getNearbyPoints(x, y, size) {
  ret = [
//    {x: x-4, y: y+2}, 
//    {x: x-3, y: y-2}, 
//    {x: x-1, y: y-1}, 
//    {x: x-1, y: y}, 
    {x: x,   y: y}, 
//    {x: x + 4, y: y + 1},
//    {x: x+4, y: y+2}, 
//    {x: x+3, y: y-2}, 
//    {x: x+1, y: y-1}, 
//    {x: x+1, y: y}, 
  ];
  return ret;
}

function draw(grid) {
//  let currentDate = new Date();
//  let time = currentDate.getHours() + ":" + currentDate.getMinutes() + ":" + currentDate.getSeconds();
//  console.log(time);
  ctx.clearRect(0, 0, grid.width, grid.height);
  ctx.strokeRect(0, 0, grid.width, grid.height);
  if(mouseIsDown) {
    const mPos = getMousePos(mouseIsDown);
    for(let pos of getNearbyPoints(mPos.x,mPos.y,randInt(4,9))) {
      grid.set(pos.x, pos.y, varyColor(SAND_COLOR));
    }
  }
  let imgData = ctx.getImageData(0, 0, cvs.width, cvs.height);
  for(let p=0; p<imgData.data.length; p+=4) {
    let c = imgDataToCoord(p, cvs.width);
    if(c.x == 0 || c.y == 0 || c.y == grid.height-1 || c.x == grid.width-1) continue;
    let color = grid.get(c.x, c.y);
    if(color) {
      imgData.data[p] = color.red;
      imgData.data[p+1] = color.green;
      imgData.data[p+2] = color.blue;
      imgData.data[p+3] = color.alpha;
    }
  }
  grid.update();
  ctx.putImageData(imgData, 0, 0); 
  window.requestAnimationFrame(draw.bind(draw, grid));
}



function randInt(min, limit) {
  let val = Math.floor(Math.random() * limit);
  return val >= min ? val : randInt(min, limit);
}


function varyColor(color) {
  return {
    red: randInt(color.red - 20, color.red + 20),
    green: randInt(color.green - 20, color.green + 20),
    blue: randInt(color.blue - 20, color.blue + 20),
    alpha: randInt(color.alpha - 20, color.alpha + 20)
  }
}

window.SAND_COLOR = {red: 220 , green: 177, blue: 89, alpha: 255 };

var cvs = document.querySelector('canvas');
var ctx = cvs.getContext('2d');
var mouseIsDown = false;
let pixelSize = 5;
cvs.width = 280;
cvs.height = 160;

grid = new Grid(cvs.width, cvs.height, pixelSize);

cvs.addEventListener('contextmenu', function(evt) {
  evt.preventDefault();
});

cvs.addEventListener('mousedown', function(evt) {
  evt.preventDefault();
  switch(evt.buttons) {
    case 2:
      grid.clear();
      break;
    default:
      mouseIsDown = evt;
      break;
  }
});

cvs.addEventListener('mouseup', function(evt) {
  evt.preventDefault();
  mouseIsDown = null;
});

cvs.addEventListener('mousemove', function(evt) {
  evt.preventDefault();
  if(mouseIsDown) {
    mouseIsDown = evt;
  }
});

//requestAnimationFrame(draw.bind(draw, grid));
const fps=1;

//function animate() {
//  setTimeout(() => {
//    requestAnimationFrame(draw.bind(draw, grid));
//  }, 1000 / fps);
//}

requestAnimationFrame(draw.bind(draw, grid));
//animate();
