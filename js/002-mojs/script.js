const bouncyCircle = new mojs.Shape({
  shape:        'circle',
  fill:         {'#F64040': '#FC46AD'},
  radius:       {20: 80},
  duration:     2000,
  isYoyo:       true,
  isShowStart:  true,
  easing:       'elastic.inout',
  repeat:       5
});
document.body.appendChild(bouncyCircle.el);
bouncyCircle.play();


const spinner = new mojs.Shape({
    parent:           '#spinner',
    shape:            'circle',
    stroke:           '#FC46AD',
    strokeDasharray:  '125, 125',
    strokeDashoffset: {'0': '-125'},
    strokeWidth:      4,
    fill:             'none',
    left:             '30px',
    top:              '30px',
    rotate:            {'-90': '270'},
    radius:           20,
    isShowStart:      true,
    duration:         2000,
    easing:           'back.in',
  })
  .then({
    rotate:            {'-90': '270'},
    strokeDashoffset: {'-125': '-250'},
    duration:         3000,
    easing:           'cubic.out',
  });
  
  spinner.play();