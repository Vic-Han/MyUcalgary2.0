<template>
    <div class="flex flex-row">
        <div class="grid grid-cols-1 grid-rows-12 text-grey-200">
            <div>8</div>
            <div>9</div>
            <div>10</div>
            <div>11</div>
            <div>12</div>
            <div>1</div>
            <div>2</div>
            <div>3</div>
            <div>4</div>
            <div>5</div>
            <div>6</div>
            <div>7</div>
        </div>
        <div class="grid grid-cols-5 grid-rows-12 bg-white-100 divide-solid div-grey-200 w-fit rounded-xl">
            <div class="w-40 bg-grey-100 text-grey-200">Monday</div>
            <div class="w-40 bg-grey-100 text-grey-200">Tuesday</div>
            <div class="w-40 bg-grey-100 text-grey-200">Wednesday</div>
            <div class="w-40 bg-grey-100 text-grey-200">Thursday</div>
            <div class="w-40 bg-grey-100 text-grey-200">Friday</div>
            <div class="w-40 text-grey-200">m8</div>
            <div class="w-40 text-grey-200">t8</div>
            <div class="w-40 text-grey-200">w8</div>
            <div class="w-40 text-grey-200">h8</div>
            <div class="w-40 text-grey-200">f8</div>
            <div class="w-40 text-grey-200">m9</div>
            <div class="w-40 text-grey-200">t9</div>
            <div class="w-40 text-grey-200">w9</div>
            <div class="w-40 text-grey-200">h9</div>
            <div class="w-40 text-grey-200">f9</div>
            <div class="w-40 text-grey-200">m10</div>
            <div class="w-40 text-grey-200">t10</div>
            <div class="w-40 text-grey-200">w10</div>
            <div class="w-40 text-grey-200">h10</div>
            <div class="w-40 text-grey-200">f10</div>
            <div class="w-40 text-grey-200">m11</div>
            <div class="w-40 text-grey-200">t11</div>
            <div class="w-40 text-grey-200">w11</div>
            <div class="w-40 text-grey-200">h11</div>
            <div class="w-40 text-grey-200">f11</div>
            <div class="w-40 text-grey-200">m12</div>
            <div class="w-40 text-grey-200">t12</div>
            <div class="w-40 text-grey-200">w12</div>
            <div class="w-40 text-grey-200">h12</div>
            <div class="w-40 text-grey-200">f12</div>
            <div class="w-40 text-grey-200">m1</div>
            <div class="w-40 text-grey-200">t1</div>
            <div class="w-40 text-grey-200">w1</div>
            <div class="w-40 text-grey-200">h1</div>
            <div class="w-40 text-grey-200">f1</div>
            <div class="w-40 text-grey-200">m2</div>
            <div class="w-40 text-grey-200">t2</div>
            <div class="w-40 text-grey-200">w2</div>
            <div class="w-40 text-grey-200">h2</div>
            <div class="w-40 text-grey-200">f2</div>
            <div class="w-40 text-grey-200">m3</div>
            <div class="w-40 text-grey-200">t3</div>
            <div class="w-40 text-grey-200">w3</div>
            <div class="w-40 text-grey-200">h3</div>
            <div class="w-40 text-grey-200">f3</div>
            <div class="w-40 text-grey-200">m4</div>
            <div class="w-40 text-grey-200">t4</div>
            <div class="w-40 text-grey-200">w4</div>
            <div class="w-40 text-grey-200">h4</div>
            <div class="w-40 text-grey-200">f4</div>
            <div class="w-40 text-grey-200">m5</div>
            <div class="w-40 text-grey-200">t5</div>
            <div class="w-40 text-grey-200">w5</div>
            <div class="w-40 text-grey-200">h5</div>
            <div class="w-40 text-grey-200">f5</div>
            <div class="w-40 text-grey-200">m6</div>
            <div class="w-40 text-grey-200">t6</div>
            <div class="w-40 text-grey-200">w6</div>
            <div class="w-40 text-grey-200">h6</div>
            <div class="w-40 text-grey-200">f6</div>
            <div class="w-40 text-grey-200">m7</div>
            <div class="w-40 text-grey-200">t7</div>
            <div class="w-40 text-grey-200">w7</div>
            <div class="w-40 text-grey-200">h7</div>
            <div class="w-40 text-grey-200">f7</div>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'SchedPreview',
        props: {
            schedule: {
                type: Object,
                required: true
            }
        }
    }
</script>