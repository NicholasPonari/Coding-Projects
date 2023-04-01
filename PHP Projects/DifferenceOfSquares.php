<?php
declare(strict_types=1);
function squareOfSum(int $max): int
{
    return (($max * ($max + 1)) / 2 ) ** 2;
}
function sumOfSquares(int $max): int
{
    return $max*($max+1)*(2*$max+1)/6;
}
function difference(int $max): int
{
    return squareOfSum($max) - sumOfSquares($max);
}